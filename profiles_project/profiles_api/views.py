from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from profiles_api.serializer import HelloSerializer
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



