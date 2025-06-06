from django.urls import path
from . import views
from .views import hello_world
from .views import HelloWorldAPIView





urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('hello/', hello_world),
    path('hello-class/', HelloWorldAPIView.as_view()),
    
]

