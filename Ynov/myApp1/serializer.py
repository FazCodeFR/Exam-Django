from myApp1.models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class MeubleSerializer(ModelSerializer):
    class Meta:
        model = Meuble
        fields = '__all__'
        # depth = 1


class MagasinSerializer(ModelSerializer):
    meubles = MeubleSerializer(many=True)

    class Meta:
        model = Magasin
        fields = '__all__'


class DirigeantSerializer(ModelSerializer):

    class Meta:
        model = Dirigeant
        fields = '__all__'
