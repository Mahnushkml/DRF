from django.shortcuts import render
from django.db import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


from profiles_api.serializer import HelloSerializer
from profiles_api import serializer
from profiles_api import models
from profiles_api import permissions

# Create your views here.

class Hello_API(APIView):
    """Test API View"""

    def get(self,request):
        return Response({"test":True}, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create hello message with our name"""
        ser = HelloSerializer(data=request.data)

        if ser.is_valid():
            name = ser.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(
                ser.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializer.HelloSerializer
    
    def list(self, request):
        "return a hello message "
        a_viewset = [
            'uses action (list, ctrate, retrieve, update, partial_update)',
            'Automatically maps to  URLs using Routers',
            'Provides more functionality with less code',
            ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    
    def create(self, request):
        """Create a new Hello message"""
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
    

class UserProfileViewSet(viewsets.ModelViewSet): 
    """Handle creating and updating profiles"""
    serializer_class = serializer.UserSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profile feed items """

    # don't forget put , after TokenAuthentication
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)