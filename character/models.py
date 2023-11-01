from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    create_date = models.DateTimeField("date created")
    def getName(self):
        return self.name + " " + self.last_name
    def __str__(self):
        return getName(self)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class CharacterSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    def __str__(self):
        return self.character