from django.urls import path, include

from rest_framework.routers import DefaultRouter
from assets import views
from .views import AssetsViewSet
# from profiles_api import views

router = DefaultRouter()
router.register(r'assets', AssetsViewSet, basename="assets")
# router.register('assets', views.AssetsListCreateView, basename='asset-list-create')
# router.register('assets/<int:pk>/', views.AssetsDetailView, basename='movie-detail')
# router.register('assets/all/', views.AllAssetsListView, basename='all-assets-list')
# router.register('assets/delete/<int:pk>/', views.AssetsDeleteView , basename='assets-delete')
# router.register('assets/update/<int:pk>/', views.AssetsUpdateView, basename='assets-update')

urlpatterns=[

    # path('assets/', views.AssetListViewSet.as_view()),
    path('', include(router.urls)),


]