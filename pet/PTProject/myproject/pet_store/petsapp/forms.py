from django import forms
from .models import PetUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PetRegistration(forms.ModelForm):
    class Meta:
        model = PetUser
        fields = ('name', 'email')
class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']