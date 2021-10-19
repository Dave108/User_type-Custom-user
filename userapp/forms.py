from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'usertype')

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'usertype': forms.Select(attrs={'class': 'form-select'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'usertype')
