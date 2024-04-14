from django.urls import path

from . import views

urlpatterns = [
    path('', views.signUp, name='signup'),
    path('signin/', views.signIn, name='signin')
]