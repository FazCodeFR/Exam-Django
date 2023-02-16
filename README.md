# Exam Django

[![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=Django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-092E20.svg?style=for-the-badge&logo=DRF&logoColor=white)](https://www.django-rest-framework.org/)
[![Swagger](https://img.shields.io/badge/Swagger-85EA2D.svg?style=for-the-badge&logo=Swagger&logoColor=black)](https://swagger.io/)
[![Git](https://img.shields.io/badge/Git-F05032.svg?style=for-the-badge&logo=Git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://git-scm.com/)

## Table des matières

- [Présentation](#présentation)
- [Stack technologique](#stack-technologique)
- [Assurance de la qualité du code](#assurance-de-la-qualité-du-code)
- [Installation](#installation)
- [Plugins conseillés](#plugins-conseillés)
- [Support/Docs](#support)

## Contexte

La filmothèque ‘LaFilmothequeDuSud’ aimerait avoir à disposition une application Web lui
permettant le suivi de ses films..
Cette application Web doit être solide, sécurisée, évolutive et avoir une bonne scalabilité.
Pour ce faire, la filmothèque a choisi une solution découplée, où une application front
correspondant à l’IHM sera développée et interagira avec une API Rest qui correspondra au
backoffice. Elle a recruté une équipe de développeurs, le problème étant que l’équipe est
staffer au maximum côté Frontend mais manque de compétence sur la partie Backend.
C’est donc dans ce cadre que vous avez été appelés en renfort pour développer l’API en
question.

## Stack technologique

- Django Rest Framework
- Sqlite3
- Swagger

# Assurance de la qualité du code

Des mesures ont été recommandées pour assurer la qualité optimale du code et faciliter son maintien. Celles-ci incluent :

- Documentation de l'API à l'aide de Swagger, ce qui permettra la génération automatique de la documentation de l'API et sa rendra plus accessible pour les utilisateurs.

- Ajout de commentaires clairs et concis au code, ce qui aidera les développeurs à comprendre son fonctionnement et à le maintenir en cas de besoin.

- Utilisation d'un Linter comme Eslint pour vérifier la qualité du code et l'adapter aux standards de codage, ce qui permettra de corriger les erreurs de syntaxe et de formatage et d'améliorer la qualité du code.

- Formatage du code avec Prettier pour le rendre plus lisible, ce qui aidera les développeurs à comprendre et à maintenir le code plus facilement.

## Installation

- Télécharger Django
  pip install Djang

- Cloner le projet

```shell
git clone https://github.com/FazCodeFR/Exam-Django.git -b laBrancheVoulu
cd Exam-Django
```

- Activer l'environnement virtuel

```shell
source path/venv/Scripts/activate

```

- Lancer le projet

```python
py manage.py runserve
```

## Plugins conseillés

Eslint : Linter
Prettier : Code formater

## Support

[Django moodle](https://moodle.ynov.com/pluginfile.php/718730/mod_resource/content/7/02.%20DJANGO.pptx.pdf)

[Consigne Examen Django DRF](https://moodle.ynov.com/pluginfile.php/724742/mod_resource/content/1/Examen%20Django%20DRF.docx.pdf)
