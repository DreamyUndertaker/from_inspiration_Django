from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.signUp, name='signup'),
    path('signin/', views.signIn, name='signin'),
    path('home', include('home.urls')),
]