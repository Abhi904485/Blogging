from PIL import Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "first_name", 'placeholder': "Enter First name",
               'name': "first_name"}), )
    last_name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "last_name", 'placeholder': "Enter Last name",
               'name': "last_name"}))
    username = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "username", 'placeholder': "Enter username",
               'name': "username"}))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(
        attrs={'class': "form-control", 'id': "email", 'placeholder': "Enter email", 'name': "email"}))
    password1 = forms.CharField(label="", required=True, widget=forms.PasswordInput(
        attrs={'class': "form-control", 'id': "password1", 'placeholder': "Enter password", 'name': "password1"}))
    password2 = forms.CharField(label="", required=True, widget=forms.PasswordInput(
        attrs={'class': "form-control", 'id': "password2", 'placeholder': "Confirm Password", 'name': "password2"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': "form-control col-md-12", 'id': "first_name", 'placeholder': "Enter First name",
               'name': "first_name"}), )
    last_name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': "form-control col-md-12", 'id': "last_name", 'placeholder': "Enter Last name",
               'name': "last_name"}))
    username = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': "form-control col-md-12", 'id': "username", 'placeholder': "Enter username",
               'name': "username"}))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(
        attrs={'class': "form-control col-md-12", 'id': "email", 'placeholder': "Enter email",
               'name': "email"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': ""
        }

    def save(self, commit=True):
        super().save()
        img = Image.open(self.instance.image.path)
        if img.height > 300 and img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.instance.image.path)
