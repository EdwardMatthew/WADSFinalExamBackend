# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .serializers import NewProdSerializer, LoginSerializer, RegisterSerializer
from .models import NewProd, Login

class LoginViewSet(viewsets.ModelViewSet): 
    queryset = Login.objects.all().order_by('username')
    serializer_class = LoginSerializer 

class NewProdViewSet(viewsets.ModelViewSet):
    queryset = NewProd.objects.all().order_by('name')
    serializer_class = NewProdSerializer 

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all().order_by('name')
    serializer_class = RegisterSerializer
