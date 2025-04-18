from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('add/', views.add_flashcard, name='add_flashcard'),
    path('practice/', views.practice_flashcard, name='practice_flashcard'),
]