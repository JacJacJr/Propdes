from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views
from . import forms

from .forms import QuestForm
from .views import *

app_name = 'Quest'
urlpatterns = [
    path('', forms.QuestForm, name='QuestForm'),
   # path('x', forms.quest, name='quest'),
    path('create/', views.quest_create, name='quest_create'),
]