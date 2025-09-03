from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput , TextInput
from .models import *
# register User
class CraeteUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1" , "password2"]


class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)
    
class CreateRecord(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
        
class UpdateRecord(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
