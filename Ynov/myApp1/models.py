from django.db import models

from django.db import models


class Realisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    pays = models.CharField(max_length=50, null=True)
    ville = models.CharField(max_length=50, null=True)


class Scenario(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    estEnEcriture = models.BooleanField(default=False)
    # Relation OneToOne avec le film
    film = models.OneToOneField(
        'Film', on_delete=models.CASCADE, related_name='film_scenario', null=True)


class Film(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    duree_minutes = models.IntegerField(null=True)
    notation = models.IntegerField(null=True)
    estAuCinema = models.BooleanField(default=False)
    # TODO: genre choice
    genre = models.CharField(max_length=50, null=True)
    # Relation OneToMany avec Realisateur
    realisateur = models.ForeignKey(
        Realisateur, on_delete=models.CASCADE, related_name='films_realises')
    # Relation OneToOne avec Scénario
    scenario = models.OneToOneField(
        Scenario, on_delete=models.CASCADE, related_name='scenario_film', null=True)


class Acteur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    # Relation ManyToMany avec le film par le biais de Jouer
    films = models.ManyToManyField(Film, through='Jouer')


class Jouer(models.Model):
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateCreationCompte = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + " " + self.prenom


class Emprunter(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    datePret = models.DateTimeField(auto_now_add=True)
    dateRetour = models.DateTimeField(null=True)
    estRendu = models.BooleanField(default=False)

    def __str__(self):
        return self.film.titre + " - " + self.client.nom + " " + self.client.prenom
