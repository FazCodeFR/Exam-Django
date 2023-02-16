from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from myApp1.serializer import *
from myApp1.models import Realisateur, Scenario, Film, Acteur, Client, Emprunter
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class IsAdminOrReadOnly(IsAdminUser):
    """
    Custom permission to only allow administrators to create, update, and delete objects.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        permission_classes = [IsAuthenticated]
        return request.user and request.user.is_staff


class RealisateurViewSet(ModelViewSet):
   # Seul l'admin peut ajouter/modifier/supprimer les données
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = RealisateurSerializer

    def get_queryset(self):
        queryset = Realisateur.objects.all()
        nom = self.request.GET.get('nom')
        prenom = self.request.GET.get('prenom')
        age = self.request.GET.get('age')
        pays = self.request.GET.get('pays')

        # Recherche par filtre
        if nom is not None:
            queryset = queryset.filter(nom=nom)
        if prenom is not None:
            queryset = queryset.filter(prenom=prenom)
        if age is not None:
            queryset = queryset.filter(age=age)
        if pays is not None:
            queryset = queryset.filter(pays=pays)
        return queryset


class ScenarioViewSet(ModelViewSet):
    serializer_class = ScenarioSerializer

    # Seul l'admin peut ajouter/modifier/supprimer les données
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Scenario.objects.all()
        titre = self.request.GET.get('titre')
        description = self.request.GET.get('description')

        # Recherche par filtre
        if titre is not None:
            queryset = queryset.filter(titre=titre)
        if description is not None:
            queryset = queryset.filter(description=description)

        return queryset


class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer

    # Seul l'admin peut ajouter/modifier/supprimer les données
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Film.objects.all()

        titre = self.request.GET.get('titre')
        description = self.request.GET.get('description')
        duree_minutes = self.request.GET.get('duree_minutes')
        genre = self.request.GET.get('genre')
        # realisateur = self.request.GET.get('realisateur')
        # scenario = self.request.GET.get('scenario')

        # Recherche par filtre
        if titre is not None:
            queryset = queryset.filter(titre=titre)
        if description is not None:
            queryset = queryset.filter(description=description)
        if duree_minutes is not None:
            queryset = queryset.filter(duree_minutes=duree_minutes)
        if genre is not None:
            queryset = queryset.filter(genre=genre)
        # if realisateur is not None:
        #     queryset = queryset.filter(realisateur=realisateur)
        # if scenario is not None:
        #     queryset = queryset.filter(scenario=scenario)

        return queryset


class ActeurViewSet(ModelViewSet):
    serializer_class = ActeurSerializer

    # Seul l'admin peut ajouter/modifier/supprimer les données
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Acteur.objects.all()

        nom = self.request.GET.get('nom')
        prenom = self.request.GET.get('prenom')
        age = self.request.GET.get('age')
        pays = self.request.GET.get('pays')
        # film = self.request.GET.get('film')

        # Recherche par filtre
        if nom is not None:
            queryset = queryset.filter(nom=nom)
        if prenom is not None:
            queryset = queryset.filter(prenom=prenom)
        if age is not None:
            queryset = queryset.filter(age=age)
        if pays is not None:
            queryset = queryset.filter(pays=pays)

        #  Récupérer la liste des acteurs ayant joué dans au moins un film avec un réalisateur donné (par l’ID)
        realisateur = self.request.GET.get('realisateur')
        if realisateur is not None:
            queryset = queryset.filter(film__realisateur=realisateur)

        # if film is not None:
        #     queryset = queryset.filter(film=film)

        return queryset


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer

    # Seul l'admin peut ajouter/modifier/supprimer les données
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Client.objects.all()

        nom = self.request.GET.get('nom')
        prenom = self.request.GET.get('prenom')
        age = self.request.GET.get('age')
        pays = self.request.GET.get('pays')

        # Recherche par filtre
        if nom is not None:
            queryset = queryset.filter(nom=nom)
        if prenom is not None:
            queryset = queryset.filter(prenom=prenom)
        if age is not None:
            queryset = queryset.filter(age=age)
        if pays is not None:
            queryset = queryset.filter(pays=pays)

        return queryset


class EmprunterViewSet(ModelViewSet):
    serializer_class = EmprunterSerializer

    # Seul l'admin peut ajouter/modifier/supprimer les données
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Emprunter.objects.all()

        date_emprunt = self.request.GET.get('date_emprunt')
        date_retour = self.request.GET.get('date_retour')
        # film = self.request.GET.get('film')
        # client = self.request.GET.get('client')

        # Recherche par filtre
        if date_emprunt is not None:
            queryset = queryset.filter(date_emprunt=date_emprunt)
        if date_retour is not None:
            queryset = queryset.filter(date_retour=date_retour)
        # if film is not None:
        #     queryset = queryset.filter(film=film)
        # if client is not None:
        #     queryset = queryset.filter(client=client)

        return queryset
