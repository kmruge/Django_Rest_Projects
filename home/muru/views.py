from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from muru.serializer import personSerializers, colorSerializer, RegisterUser, LogInAuthSerializer, passwordChangeSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import person,color
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from muru.permission import personPermission
# Create your views here.

@api_view(['GET','POST'])
def index(request):
    if request.method =='POST':
        data=request.data
        mess='This is POST Method'
        dict={
            'name':data["name"],
            'age':data["age"],
            'message':mess
        }
        print(mess)
        return Response(dict)
    elif request.method =='GET':
        mess='This is GET Method'
        dict={
            'name':'Aishu',
            'age':26,
            'message':mess
        }
        print(mess)
        return Response(dict)

@api_view(['GET','POST','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def personView(request):
    if request.method=='POST':
        data=request.data
        serialiser=personSerializers(data=data)
        if serialiser.is_valid():
          serialiser.save()
          return Response(serialiser.data,status=status.HTTP_201_CREATED)
        return Response(serialiser.errors)
    elif request.method=='GET':
        try:
          data=person.objects.all()
          print(request.user.id)
          page=request.GET.get('page',1)
          page_size=5
          paginator=Paginator(data,page_size)
          serialiser=personSerializers(paginator.page(page), many=True)
          count=len(serialiser.data)
          return Response({"Count":count,
               "data":serialiser.data})
        except Exception:
             return Response({
                  "Status":False,
                  "Message":"Invalid Page Number"
             }
             )
    elif request.method=='DELETE':
         data=data=person.objects.all()
         data.delete()
         return Response("All data wiped off Successfully")
    return Response(serialiser.errors)

@api_view(['POST','GET','PATCH','PUT','DELETE'])
def edit_info(request,pk):
        
          dataObj=person.objects.get(id=pk)
          data=request.data
          
          if request.method=='GET':
               serializer=personSerializers(dataObj)
               return Response(serializer.data)
          elif request.method=='PATCH':
               serializer=personSerializers(dataObj,data=data,partial=True)
               if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
          elif request.method=='PUT':
               serializer=personSerializers(dataObj,data=data)
               if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
          elif request.method=='DELETE':
               dataObj.delete()
               return Response("Object Deleted Successfully")
               
          return Response(serializer.errors)

class Color_view(APIView):
         def get(self,request):
              color1=color.objects.all()
              serialiser=colorSerializer(color1,many=True)
              return Response(serialiser.data)
         def post(self,request):
              data=request.data
              serializer=colorSerializer(data=data)
              if serializer.is_valid():
                   serializer.save()
                   return Response(serializer.data,status=status.HTTP_201_CREATED)
              
class Color_view_edit(APIView):
     
     def get(self,request,pk):
          try:
               color1=color.objects.get(id=pk)
          except:
               return Response("This Object doesn't exist")
          serialiser=colorSerializer(color1)
          return Response(serialiser.data)
     def patch(self,request,pk):
          reqdata=request.data
          try:
           color1=color.objects.get(id=pk)
          except:
               return Response("This object not present")
          serialiser=colorSerializer(color1,data=reqdata,partial=True)
          if serialiser.is_valid():
               serialiser.save()
               return Response(serialiser.data)

#It perform CRUD operations without defining methods like APIViews and @api_view
#Serializer and queryset are overwritten from base class. Check the declaration of this ModelViewSet 
# to finds out about create, list, updata, destroy. All these methods can be overwritten based on our desires
# 
class PersonModelViewSet(viewsets.ModelViewSet):
     serializer_class=personSerializers
     queryset=person.objects.all()

     # We can't limit the request type in modelsViewSet like @api_view, APIView, ViewSet(create, list, retrieve etc)
     # To have request limitation, we need to use http_method_names
     http_method_names = ['get', 'post', 'patch']

     def list(self,request):
          search=request.GET.get('search')
          queryset=self.queryset
          if search:
               queryset=queryset.filter(Name__startswith=search)
          serializer=personSerializers(queryset,many=True)
          return Response(serializer.data)
     
     
class personViewSet(viewsets.ViewSet):
     # permission_classes = [IsAuthenticated]
     # authentication_classes = [TokenAuthentication]
     #Create instance in model class
     def create(self, request):
          serializer=personSerializers(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors)
     #Get specific instance of the models
     def retrieve(self,request,pk=None):
          queryset=person.objects.all()
          instance = get_object_or_404(queryset, pk=pk)
          serializer=personSerializers(instance)
          return Response(serializer.data)
     #To Retrieve all instances of the model class
     def list(self,request):
          queryset=person.objects.all()
          serializer=personSerializers(queryset,many=True)
          return Response(serializer.data)
     
     # Action decorator only for ViewSet. We can have custom function inside the Viewset class.
     # detail=False pk should not be passed in the function. URL look like http://127.0.0.1:1909/api/personViewSet/send_email/
     # detail=True pk value should be present in the function. URL look like http://127.0.0.1:1909/api/personViewSet/1/send_email/

     @action(detail=False, methods=['post'])
     def send_email(self, request, pk):
          return Response('Email is sent')
     
class registerUser(APIView):

     def post(self,request):
          data=request.data
          serializer=RegisterUser(data=data)
          if not serializer.is_valid():
               return Response({
                    "status":False,
                    "descri":serializer.errors
               })
          serializer.save()
          return Response({
               "User is created sucessfully"
          })

class passChange(APIView):
     permission_classes = [IsAuthenticated]
     authentication_classes = [TokenAuthentication]
     def patch(self,request):
          print(request.user)
          data=request.data
          serializer=passwordChangeSerializer(data=data)
          if serializer.is_valid():
               serializer.update(serializer.data)
               # user=User.objects.get(username=data['username'])
               # user.set_password(data['newpassword'])
               # serializer.save()
               return Response("Password changed sucessfully")
          
          return Response(serializer.errors)

class LogInAuth(APIView):

     def post(self,request):
          data=request.data
          serializer=LogInAuthSerializer(data=data)
          if not serializer.is_valid():
               return Response({
                    "status":False,
                    "descri":serializer.errors
               })
          user=authenticate(username=data['username'],password=data['password'])
          if not user:
               return Response("Invalid Credential")
          token,_=Token.objects.get_or_create(user=user)
          # refresh = RefreshToken.for_user(user)
          return Response({
               "User":data['username'],
               "token":str(token),
               # "refresh Toke": {'refresh': str(refresh), 'access': str(refresh.access_token)}
          })
     
class showPersonDetails(viewsets.ViewSet):
     serializer=personSerializers
     queryset=person.objects.all()
     permission_classes = [IsAuthenticated, personPermission]
     authentication_classes = [BasicAuthentication, TokenAuthentication]
     def list(self, request):
          serializer=personSerializers(self.queryset, many=True)
          return Response(serializer.data)
     
     def retrieve(self, request, pk):
          obj=get_object_or_404( self.queryset, pk=pk)
          # we can usr check object permission to check the permission for the specific object (has_object_permission)
          self.check_object_permissions(request, obj)
          serializer=personSerializers(obj)
          return Response({"test":"test", "value":serializer.data})

     # this get_object can be reused for retrieve, destroy, update, partial_update
     def get_object(self, pk):
          obj=get_object_or_404(self.queryset, pk=pk)
          return obj
     
     def destroy(self, request, pk):
          obj=self.get_object(pk)
          obj.delete()
          return Response("Object Deleted Successfully")
