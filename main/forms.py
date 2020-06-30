from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class CreateUserForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            
        }
