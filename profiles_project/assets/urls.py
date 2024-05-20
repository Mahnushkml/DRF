from django.urls import path, include

from rest_framework.routers import DefaultRouter
from assets import views
# from profiles_api import views

router = DefaultRouter()
router.register('list', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemViewSet)

urlpatterns=[

    # path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]