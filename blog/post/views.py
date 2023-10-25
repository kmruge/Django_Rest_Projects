from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import postSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import blog
from rest_framework import status
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.core.paginator import Paginator
from rest_framework.decorators import action
# Create your views here.

class post_Blog(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self,request):
        data=request.data.copy()
        data['user']=request.user.id
        serializer=postSerializers(data=data)
        if not serializer.is_valid():
            return Response({"Status":"Failed",
                             "description":serializer.errors})
        serializer.save()
        return Response(serializer.data)
    def get(self,request):
        try:
            blogs=blog.objects.filter(user=request.user)
            if request.GET.get('search'):
                print(1)
                search=request.GET.get('search')
                blogs=blogs.filter(Q(title__icontains=search) | Q(content__icontains=search))
            serializer=postSerializers(blogs,many=True)
            return Response({
                'data':serializer.data,
                'message':'Blog Fetched Successfully'
            })
        except Exception as e:
            print(e)
            return Response("Something went wrong",status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request):
        try:
            data=request.data
            obj=blog.objects.get(id=data['id'])
            serializer=postSerializers(obj,data=data,partial=True)
            if not serializer.is_valid():
                return Response({
                    "Detail":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response("Something went wrong")
        
    def delete(self,request):
        data=request.data
        obj=blog.objects.get(UUID=data['uuid'])
        if not obj:
            return Response("Requested blog not found")
        obj.delete()
        return Response("Deleted Successfully")

class APIListCreatelistView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset=blog.objects.all()
    serializer_class=postSerializers


    def create(self,request):
        data=request.data
        data['user']=request.user.id
        """here if we call the repective serializer to perform the action, will error out saying
        querySet is immutable. We always have to use self.queryset to refer instance to perform 
        query and self.get_serializer to call repective serializer for validating and saving the data"""
        serializer=self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
    def list(self,request):
        page=request.query_params.get('page',1)
        page_size=3
        paginator=Paginator(self.queryset,page_size)
        serializer=self.get_serializer(paginator.page(page), many=True)
        return Response({"Count":blog.objects.all().count(), "Result":serializer.data})
    
class listcreatecviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]
    # IsAdminUser is restrict the function to access agent present in the db.
    queryset=blog.objects.all()
    serializer_class=postSerializers
    
    #This is another way of performing query set. We can user get_queryset to specifically queryset the data
    def get_queryset(self,search):
        return blog.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
    
    def create(self,request):
        data=request.data
        data['user']=request.user.id
        serializer=self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(serializer._errors)
        serializer.save()
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        search=request.query_params.get('search')
        if search:
            self.queryset=self.get_queryset(search)
        page=request.query_params.get('page',1)
        page_size=2
        paginator=Paginator(self.queryset,page_size)
        serializer=self.get_serializer(paginator.page(page), many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def list_latest(self,request):
        query=self.queryset.filter().order_by('title')
        print("entered")
        serializer=self.get_serializer(query, many=True)
        return Response(serializer.data)