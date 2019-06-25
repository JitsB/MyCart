from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # name = forms.CharField(max_length = 50)
    address = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 50, help_text = "Required.")

    class Meta:
        model = User
        fields = ('username','address','email','password1','password2')

