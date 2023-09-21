from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import postSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import post
from rest_framework import status
from django.db.models import Q
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
            blogs=post.objects.filter(user=request.user)
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
            obj=post.objects.get(UUID=data['uuid'])
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
        obj=post.objects.get(UUID=data['uuid'])
        if not obj:
            return Response("Requested blog not found")
        obj.delete()
        return Response("Deleted Successfully")

