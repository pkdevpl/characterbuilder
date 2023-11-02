from django.shortcuts import render, get_object_or_404, redirect
from .models import Character

def index(request):
    if request.user.is_authenticated:
        characters = Character.objects.all()
        return render(request, "character/index.html", {"list": characters, "user": request.user})
    else:
        return redirect("user:login")


def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, "character/details.html", {"character": character})

def form(request):
    return render(request, "character/form.html")


class CharacterForm:
    pass


def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user  # Ustaw użytkownika na zalogowanego użytkownika
            character.save()
            return redirect('character_detail', character.id)  # Przekieruj do widoku szczegółów postaci
    else:
        form = CharacterForm()

    return render(request, 'character/../templates/create_character.html', {'form': form})