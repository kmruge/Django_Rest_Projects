from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountSerializer, loginSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Register(APIView):

    def post(self,request):
        try:
            data=request.data
            serialiser=AccountSerializer(data=data)
            if not serialiser.is_valid():
                return Response({
                    "Error": serialiser.errors,
                    "Description":"Something went wrong"
                }, status=status.HTTP_400_BAD_REQUEST)
            serialiser.save()
            print("enter-3")
            return Response({
                "Message":"Account created"
            },status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message":"Something went wrong"
            })
        
class login(APIView):
    def post(self,request):
        data=request.data
        serializer=loginSerializer(data=data)
        if not serializer.is_valid():
            return Response({"message":serializer.errors})
        token=serializer.get_jwt_token(data)
        return Response({
            "Status":"Token Create sucessfuly",
            "Token":token
        })
        
