from django.shortcuts import render
import random
# Create your views here.
from django.shortcuts import render, redirect
from .forms import FlashcardForm
from .models import Flashcard


def add_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_flashcard') #refresh page to clear form
    else: 
        form = FlashcardForm()

    return render(request, 'core/add_flashcard.html', {'form': form})

def practice_flashcard(request):
    flashcards = Flashcard.objects.all()
    flashcard = random.choice(flashcards) if flashcards else None
    return render(request, 'core/practice.html', {'flashcard': flashcard})

def welcome_page(request):
    return render(request, 'core/welcome.html')