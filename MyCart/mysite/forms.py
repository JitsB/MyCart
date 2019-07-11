from django import forms
from .models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','email','address')


class LoginForm(forms.Form):
    Username = forms.CharField(max_length = 20)
    Password = forms.CharField(max_length = 20, widget = forms.PasswordInput)
