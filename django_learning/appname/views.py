from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from appname.models import profile, blood
from appname.serializers import profileSerializer


class bio(APIView):
    def get(self, request):
        query=profile.objects.all()
        print(query)
        serializer=profileSerializer(query, many=True)
        return Response(serializer.data)