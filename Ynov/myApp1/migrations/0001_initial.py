# Generated by Django 4.1.5 on 2023-02-03 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dirigeant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Magasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('CA', models.IntegerField()),
                ('dirigeant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dirigeant', to='myApp1.dirigeant')),
            ],
        ),
        migrations.CreateModel(
            name='Meuble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('etat', models.CharField(choices=[('NEUF', 'NEUF'), ('OCCASION', 'OCCASION'), ('MAUVAIS ETAT', 'MAUVAIS ETAT'), ('INUTILISABLE', 'INUTILISABLE')], default='NEUF', max_length=50)),
                ('prix', models.IntegerField()),
                ('statut', models.CharField(choices=[('LIBRE', 'LIBRE'), ('VENDU', 'VENDU')], default='LIBRE', max_length=50)),
                ('lieu_stockage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='magasin', to='myApp1.magasin')),
            ],
        ),
    ]
