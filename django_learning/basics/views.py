from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import profileSerializerModel, profileSerializer
from rest_framework.response import Response
from .models import fieldsLearning
from rest_framework import status

@api_view(['GET','POST'])
def profile(request):

    if request.method=='GET':
        try:
            data=fieldsLearning.objects.all()
        except fieldsLearning.DoesNotExist:
            return Response("No data found", status=status.HTTP_404_NOT_FOUND)
        serializer=profileSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        data=request.data
        serializer=profileSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PATCH','DELETE'])
def profile_obj(request,pk):
    if request.method=='GET':
        try:
            obj=fieldsLearning.objects.get(id=pk)
        except fieldsLearning.DoesNotExist:
            return Response("No data found", status=status.HTTP_404_NOT_FOUND)
        serializer=profileSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='PATCH':
        try:
            obj=fieldsLearning.objects.get(id=pk)
        except fieldsLearning.DoesNotExist:
            return Response("No data found", status=status.HTTP_404_NOT_FOUND)
        data=request.data
        serializer=profileSerializer(obj, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        try:
            obj=fieldsLearning.objects.get(id=pk)
        except fieldsLearning.DoesNotExist:
            return Response("No data found", status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)
# Create your views here.
@api_view(['GET','POST'])
def profileModel(request):
    if request.method == 'POST':
        data=request.data
        serializer=profileSerializerModel(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'GET':
        data=fieldsLearning.objects.all()
        serializer=profileSerializerModel(data, many=True)
        return Response(serializer.data)

@api_view(['GET','PATCH','DELETE'])
def profile_obj_model(request, pk):
    if request.method == 'GET':
        data=fieldsLearning.objects.get(id=pk)
        serializer=profileSerializerModel(data)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        data=request.data
        obj=fieldsLearning.objects.get(id=pk)
        serializer=profileSerializerModel(obj, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        obj=fieldsLearning.objects.get(id=pk)
        obj.delete()
        return Response("Deleted Successfully")