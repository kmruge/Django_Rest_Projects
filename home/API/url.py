"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from muru.views import index, personView
from muru.views import edit_info, Color_view,Color_view_edit,PersonModelViewSet,personViewSet,registerUser,LogInAuth, passChange
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'personModelViewSet',PersonModelViewSet,basename='personModelViewSet')
router.register(r'personViewSet',personViewSet,basename='personViewSet')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('index/',index, name="index"),
    path('person/',personView,name="person"),
    path('edit_info/<int:pk>/',edit_info,name="edit_info"),
    path('personViewClass/',Color_view.as_view()),
    path('personViewClass/<int:pk>/',Color_view_edit.as_view()),
    path('registeruser/',registerUser.as_view()),
    path('login/',LogInAuth.as_view()),
    path('passwordchange/', passChange.as_view()),
]