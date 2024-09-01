from django.db import models

# Create your models here.
class Pet(models.Model):
    gender=(("male","male"),("female","female"))
    image=models.ImageField(upload_to="media")
    name=models.CharField(max_length=30)
    species=models.CharField(max_length=30)
    breed=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30,choices=gender)
    description=models.CharField(max_length=500)

class PetUser(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()