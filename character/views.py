from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Character

def index(request):
    if request.user.is_authenticated == False:
        return redirect("user:login")
    characters = Character.objects.all()
    return render(request, "character/index.html", {"list": characters, "user": request.user})

def detail(request, character_id):
    if request.user.is_authenticated == False:
        return redirect("user:login")
    character = get_object_or_404(Character, pk=character_id)
    return render(request, "character/details.html", {"character": character})

class CharacterForm(forms.Form):
    name = forms.CharField(label="Imię", max_length=100)
    last_name = forms.CharField(label="Nazwisko", max_length=100)
    race = forms.CharField(label="Rasa", max_length=100)
    characterClass = forms.CharField(label="Klasa", max_length=100)
    level = forms.CharField(label="Poziom", max_length=100)

def create(request):
    if request.user.is_authenticated == False:
        return redirect("user:login")

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            # TODO: dodać do formularza postaci pole wyboru skillów, profesji itd. i zapisać poniżej w polach
            character = Character.objects.create(
                name = form.cleaned_data["name"],
                last_name = form.cleaned_data["last_name"],
                race = form.cleaned_data["race"],
                exp = 0,
            )
            return redirect('character:detail', character.id)
        return render(request, 'character/form.html', {"error_message": "Form is invalid"})
    else:
        form = CharacterForm()
        return render(request, 'character/form.html', {"form": form})

