from django.urls import path
from .views import Hello_API

urlpatterns=[
    path('hello-api/', Hello_API.as_view()),
]