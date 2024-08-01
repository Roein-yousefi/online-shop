from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from . import models

class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = models.CustomUser
        fields = ('username' , 'email')

class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = models.CustomUser
        fields = ('username' , 'email')