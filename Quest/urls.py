from django.urls import path

from . import views

app_name = 'Quest'
urlpatterns = [
    path('', views.quest, name='quest'),
]