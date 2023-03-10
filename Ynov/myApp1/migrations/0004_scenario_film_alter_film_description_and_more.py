# Generated by Django 4.1.5 on 2023-02-16 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0003_remove_scenario_film_jouer_acteur_films'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='film',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_scenario', to='myApp1.film'),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='realisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films_realises', to='myApp1.realisateur'),
        ),
        migrations.AlterField(
            model_name='film',
            name='scenario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scenario_film', to='myApp1.scenario'),
        ),
        migrations.AlterField(
            model_name='film',
            name='titre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='titre',
            field=models.CharField(max_length=100),
        ),
    ]
