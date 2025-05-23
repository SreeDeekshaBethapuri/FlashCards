from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('add/', views.add_flashcard, name='add_flashcard'),
    path('practice/', views.practice_flashcards, name='practice_flashcards'),
    path('get_new_flashcard/', views.get_new_flashcard, name='get_new_flashcard'),
]