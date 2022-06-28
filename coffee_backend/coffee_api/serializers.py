from .models import Login, NewProd  
from rest_framework import serializers 

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login 
        fields = ('email', 'password')

class NewProdSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewProd
        fields = ('name', 'desc')
