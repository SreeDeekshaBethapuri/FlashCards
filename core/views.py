from django.shortcuts import render, redirect
from .forms import FlashcardForm
from .models import Flashcard
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random, json

def add_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_flashcard')
    else:
        form = FlashcardForm()
    return render(request, 'core/add_flashcard.html', {'form': form})

def welcome_page(request):
    return render(request, 'core/welcome.html')

def practice_flashcards(request):
    flashcards = Flashcard.objects.all()
    flashcard = random.choice(flashcards) if flashcards else None
    return render(request, 'core/practice.html', {'flashcard': flashcard})

@csrf_exempt
def get_new_flashcard(request):
    if request.method == "POST":
        data = json.loads(request.body)
        shown_ids = data.get("shown_ids", [])
        flashcard = Flashcard.objects.exclude(id__in=shown_ids).order_by('?').first()
        if flashcard:
            return JsonResponse({
                "id": flashcard.id,
                "keyword": flashcard.keyword,
                "definition": flashcard.definition,
            })
        else:
            return JsonResponse({})
    return JsonResponse({"error": "Invalid request"}, status=400)
