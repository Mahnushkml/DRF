from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters

from .models import Assets
from assets.serializer import AssetsSerializer


class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer


# #############################################

# class AssetsListCreateView(viewsets.ViewSet):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer
    
    
# class AssetsDetailView(viewsets.ViewSet):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer
    
# class AllAssetsListView(viewsets.ViewSet):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer
    
# class AssetsDeleteView(viewsets.ViewSet):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer
#     partial = True
    
    
# class AssetsUpdateView(viewsets.ViewSet):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(print("delete Asset"))
    
########################################################


# class AssetListViewSet(viewsets.ViewSet):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer
    
#     def list(self, request, **kwargs):
#         queryset = Assets.objects.all()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         """Create a asset"""
#         ser2 = self.serializer_class(data=request.data)

#         if ser2.is_valid():
#             ip = ser2.validated_data.get('ip')
#             return Response ({'ip': ip})
        
#         else:
#             return Response(
#                 ser2.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        

#     def retrieve(self, request, pk=None):
#         """Handle getting an object by its ID"""
#         return Response({'http_method':'GET'})
    
#     def update(self, request, pk=None):
#         """Handle upddating an object"""
#         return Response({'http_method':'PUT'})
    
#     def partial_update(self, request, pk=None):
#         """Handle upddating part of an object"""
#         return Response({'http_method':'PATCH'})
    
#     def defstroy(self, request, pk=None):
#         """Handle removing of an object"""
#         return Response({'http_method':'DELETE'})
    

# class AssetRetrieveUpdateDestroy(viewsets.RetrieveUpdateDestroyAPIView):
#     queryset = Assets.objects.all()
#     serializer_class = AssetsSerializer