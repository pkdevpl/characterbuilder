from django.db import models
from django.contrib.auth.models import User  # Import modelu użytkownika
from django.urls import reverse

# Model dla postaci
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacja jeden do wielu z użytkownikiem
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    level = models.IntegerField()

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])

# Model dla umiejętności postaci (wiele do wielu)
class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    characters = models.ManyToManyField(Character, related_name='skills')

# Model dla ekwipunku postaci (jeden do wielu)
class InventoryItem(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='inventory')
    name = models.CharField(max_length=100)
    description = models.TextField()

# Model dla historii postaci (jeden do wielu)
class CharacterHistory(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, related_name='history')
    backstory = models.TextField()
    notes = models.TextField()

# Model dla przyjaciół postaci (wiele do wielu)
class Friend(models.Model):
    name = models.CharField(max_length=100)
    characters = models.ManyToManyField(Character, related_name='friends')