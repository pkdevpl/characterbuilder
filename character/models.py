# TODO: Znaleźć jak robi się Join w django, żeby połączyć parę modeli w jedną listę, np. Party z PartyCharacter i Character

from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=50)
    short = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Party(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gold = models.IntegerField()
    def getCharacters(self):
        # TODO: Character.objects.all()
        # then filter, where Character.party == self
        # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#select-related
        return None

class Character(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    exp = models.IntegerField(default=0)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    def getName(self):
        return self.name + " " + self.last_name
    def getLevel(self):
        # TODO: Tutaj znaleźć funkcję w stylu Math.floor, żeby zwróciła liczbę całkowitą, zamiast 1,3 level
        # return floor(exp / 1000)
        return
    def __str__(self):
        return getName(self)

class Quest(models.Model):
    name = models.CharField(max_length=50)
    minLevel = models.IntegerField(default=1)
    exp = models.IntegerField(default=200)
    gold = models.IntegerField(default=200)
    time = models.IntegerField(default=10000)
    def getByLevel(self, level):
        # pobierz wszystkie i odfiltruj <= level
        return

class CharacterQuest(models.Model):
    QUEST_STATUS = [
        ('completed', 'Completed'),
        ('pending', 'Pending')
    ]
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    timeStart = models.DateField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=10, choices=QUEST_STATUS, default='pending')
    def complete(self):
        currentTime = time.time()
        # if (currentTime > (timeStart + quest.time)) {
        #    super().save(update_fields=["status"])
        #}
        return
