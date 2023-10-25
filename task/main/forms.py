from django import forms
from .models import CustomUser, CustomGroup


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'user_group']


class GroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = ['name', 'description']