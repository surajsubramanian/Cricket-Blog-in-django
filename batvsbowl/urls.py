from django.urls import path

from . import views

urlpatterns = [
    path('ipl/batvsbowl', views.batvsbowl, name='batvsbowl'),
    path('ipl/results', views.results, name='results')
]
