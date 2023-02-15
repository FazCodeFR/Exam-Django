from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from myApp1.serializer import *
from myApp1.models import Dirigeant, Magasin, Meuble


class DirigeantViewSet(ModelViewSet):
    serializer_class = DirigeantSerializer

    # permission_classes = [IsAuthenticated]

    magasins = MagasinSerializer(many=True, read_only=True)

    def get_queryset(self):
        queryset = Dirigeant.objects.all()

        nom = self.request.GET.get('nom')
        prenom = self.request.GET.get('prenom')

        if nom is not None:
            queryset = queryset.filter(nom=nom)

        if prenom is not None:
            queryset = queryset.filter(prenom=prenom)

        return queryset


class MagasinViewSet(ModelViewSet):
    serializer_class = MagasinSerializer
    permission_classes = [IsAuthenticated]

    # dirigeant = DirigeantSerializer(read_only=True)
    # meubles = MeubleSerializer(many=True, read_only=True)

    def get_queryset(self):
        queryset = Magasin.objects.all()

        nom = self.request.GET.get('nom')
        adresse = self.request.GET.get('adresse')
        dirigeant = self.request.GET.get('dirigeant')
        CA = self.request.GET.get('CA')

        if nom is not None:
            queryset = queryset.filter(nom=nom)
        if adresse is not None:
            queryset = queryset.filter(adresse=adresse)
        if dirigeant is not None:
            queryset = queryset.filter(dirigeant=dirigeant)
        if CA is not None:
            queryset = queryset.filter(CA=CA)

        return queryset


class MeubleViewSet(ModelViewSet):
    # lieu_stockage = MagasinSerializer(read_only=True)
    serializer_class = MeubleSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Meuble.objects.all()

        nom = self.request.GET.get('nom')
        etat = self.request.GET.get('etat')
        lieu_stockage = self.request.GET.get('lieu_stockage')
        prix = self.request.GET.get('prix')
        statut = self.request.GET.get('statut')

        if nom is not None:
            queryset = queryset.filter(nom=nom)
        if etat is not None:
            queryset = queryset.filter(etat=etat)
        if lieu_stockage is not None:
            queryset = queryset.filter(lieu_stockage=lieu_stockage)
        if prix is not None:
            queryset = queryset.filter(prix=prix)
        if statut is not None:
            queryset = queryset.filter(statut=statut)

        return queryset

    # def create(self, request, *args, **kwargs):
    #     print('iciiiiiiiiiiii', request.data)
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         meuble = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
