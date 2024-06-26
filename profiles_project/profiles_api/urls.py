from django.urls import path, include
# from .views import Hello_API

from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemViewSet)

urlpatterns=[
    path('hello-api/', views.Hello_API.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]