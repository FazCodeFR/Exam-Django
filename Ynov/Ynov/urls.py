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
from myApp1.views import DirigeantViewSet, MagasinViewSet, MeubleViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view


# import ArtisteApiRest
# from myApp1.views import ArtisteApiRest


router = routers.SimpleRouter()
router.register('dirigeants', DirigeantViewSet, basename='dirigeants')
router.register('magasins', MagasinViewSet, basename='magasins')
router.register('meubles', MeubleViewSet, basename='meubles')

schema_view = get_swagger_view(title='API Documentation')


# Dirigeant, Magasin, Meuble
urlpatterns = [
    # path('admin/', admin.site.urls),

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
