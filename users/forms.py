from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'team',)

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'team', 'profile_pic']