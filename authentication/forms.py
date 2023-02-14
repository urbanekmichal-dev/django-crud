from django import forms
import datetime

from django.contrib.auth.forms import UserCreationForm

from authentication.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(),
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    department =  forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user