from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class Hello_API(APIView):
    def get(self,request):
        return Response({"test":True}, status=status.HTTP_200_OK)