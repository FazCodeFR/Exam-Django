from django.db import models


# • Un Dirigeant à un nom et un prenom
class Dirigeant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom + ' ' + self.prenom


# • Un Magasin à un nom, une adresse, un Dirigeant, un CA (Chiffre d’affaire)
class Magasin(models.Model):
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    dirigeant = models.ForeignKey(
        Dirigeant, related_name='dirigeant', on_delete=models.PROTECT)

    CA = models.IntegerField()

    def __str__(self):
        return self.nom + ' ' + self.adresse + ' ' + self.dirigeant.nom + ' ' + self.dirigeant.prenom + ' ' + str(self.CA)


# Un Meuble à un nom, un état (NEUF, OCCASION, MAUVAIS ETAT, INUTILISABLE), un lieu de stockage
# (Magasin), un prix et une statut (LIBRE, VENDU)
class Meuble(models.Model):
    nom = models.CharField(max_length=50)
    ETAT = [('NEUF', 'NEUF'), ('OCCASION', 'OCCASION'),
            ('MAUVAIS ETAT', 'MAUVAIS ETAT'), ('INUTILISABLE', 'INUTILISABLE')]
    etat = models.CharField(max_length=50, choices=ETAT, default='NEUF')
    lieu_stockage = models.ForeignKey(
        Magasin, related_name='meubles', on_delete=models.PROTECT, null=True)
    prix = models.IntegerField()
    STATUT = [('LIBRE', 'LIBRE'), ('VENDU', 'VENDU')]
    statut = models.CharField(max_length=50, choices=STATUT, default='LIBRE')

    def __str__(self):
        return self.nom
