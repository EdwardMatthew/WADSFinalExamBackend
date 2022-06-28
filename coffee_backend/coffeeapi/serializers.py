from .models import Login, NewProd  
from rest_framework import serializers 

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login 
        fields = ('email', 'password')

class NewProdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewProd
        fields = ('name', 'desc')

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ('email', 'password')
