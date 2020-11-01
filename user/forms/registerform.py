from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

from user.choices import *


class RegisterForm(UserCreationForm):
    username = UsernameField(label=_("Username"), widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}))
    email = forms.EmailField(max_length=254, label="E-mail", widget=forms.EmailInput(
        attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}),
                             validators=[EmailValidator])
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE, required=True, widget=forms.Select(
        attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-4 bg-white rounded"}))
    checkbox = forms.BooleanField(label="Accept terms and conditions.", required=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2", 'account_type', 'checkbox',)
