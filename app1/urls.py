from django.urls import path

from . import views

urlpatterns = [
    path('audio/', views.Audio_store),
    #  now file should be saved with this settings

    path('', views.Audio_store),
    path('audio/result/', views.result),
]