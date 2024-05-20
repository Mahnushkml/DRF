from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters

from .models import Assets
from assets.serializer import AssetsSerializer

class AssetListViewSet(viewsets.ViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

    def list(self, request):
        "return list of assets "
        a_viewset = [
            'uses action (list, ctrate, retrieve, update, partial_update)',
            'Automatically maps to  URLs using Routers',
            'Provides more functionality with less code',
            ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    
    def create(self, request):
        """Create a asset"""
        ser2 = self.serializer_class(data=request.data)

        if ser2.is_valid():
            name = ser2.validated_data.get('name')
            message = f'Hello {name}!'
            return Response ({'message': message})
        else:
            return Response(
                ser2.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Handle upddating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle upddating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def defstroy(self, request, pk=None):
        """Handle removing of an object"""
        return Response({'http_method':'DELETE'})
    

class AssetRetrieveUpdateDestroy(viewsets.RetrieveUpdateDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer