# Generated by Django 4.1.5 on 2023-02-16 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('duree_minutes', models.IntegerField()),
                ('genre', models.CharField(choices=[('ACTION', 'ACTION'), ('COMEDIE', 'COMEDIE'), ('DRAME', 'DRAME'), ('HORREUR', 'HORREUR')], default='ACTION', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Realisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('pays', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scenarios', to='myApp1.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='realisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='films', to='myApp1.realisateur'),
        ),
        migrations.AddField(
            model_name='film',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='films', to='myApp1.scenario'),
        ),
    ]
