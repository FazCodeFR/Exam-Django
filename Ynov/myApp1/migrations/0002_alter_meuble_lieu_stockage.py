# Generated by Django 4.1.5 on 2023-02-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meuble',
            name='lieu_stockage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='meubles', to='myApp1.magasin'),
        ),
    ]
