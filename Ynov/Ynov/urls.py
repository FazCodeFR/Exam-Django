"""Ynov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myApp1.views import RealisateurViewSet, ScenarioViewSet, FilmViewSet, ActeurViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view


# import ArtisteApiRest
# from myApp1.views import ArtisteApiRest


router = routers.SimpleRouter()
router.register('realisateurs', RealisateurViewSet, basename='realisateurs')
router.register('scenarios', ScenarioViewSet, basename='scenarios')
router.register('films', FilmViewSet, basename='films')
router.register('acteurs', ActeurViewSet, basename='acteurs')

schema_view = get_swagger_view(title='API Documentation')


# Meuble
urlpatterns = [
    # swagger
    path('api-docs/', schema_view),
    # rest_framework
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/artistes',ArtisteApiRest.as_view())
]
