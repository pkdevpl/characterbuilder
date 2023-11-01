from django.shortcuts import render, get_object_or_404
from .models import Character

def index(request):
    characters = Character.objects.all()
    return render(request, "character/index.html", {"list": characters})

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, "character/details.html", {"character": character})

def form(request):
    return render(request, "character/form.html")