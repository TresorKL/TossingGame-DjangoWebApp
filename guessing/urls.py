from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('outcome/',views.determineoutcome, name='outcome'),
    path('playagain/',views.playAgain,name='playagain'),
    path('summary/', views.determineSummary,name='summary')
]
