from django import forms
from user.models import Profile
from user.choices import *

from tinymce.widgets import TinyMCE


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Name",
        max_length=150,
        help_text="Your name",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}),
        required=False,
    )

    last_name = forms.CharField(
        label="Last name",
        max_length=150,
        help_text="Your last name",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}),
        required=False,
    )

    photo = forms.ImageField(
        label="Profile photo",
        help_text="We accept: jpg, bmp, png, etc.",
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control form-control pr-3 shadow p-1 mb-1 bg-white rounded"}), required=False,
    )

    facebook_url = forms.URLField(
        label="Facebook",
        max_length=500,
        help_text="Your Facebook",
        widget=forms.URLInput(
            attrs={"class": "form-control form-control-lg pr-5 shadow p-2 mb-1 bg-white rounded"}), required=False,

    )

    website_url = forms.URLField(
        label="Your website",
        max_length=500,
        help_text="Your personal website",
        widget=forms.URLInput(attrs={"class": "form-control form-control-lg pr-5 shadow p-2 mb-1 bg-white rounded"}),
        required=False,
    )

    about = forms.CharField(
        label="About you",
        max_length=500,
        help_text="Your bio",
        widget=TinyMCE(attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}),
        required=True,
    )

    account_type = forms.ChoiceField(
        choices=ACCOUNT_TYPE,
        required=True,
        widget=forms.Select(attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-4 bg-white rounded"}),
    )


    class Meta:
        model = Profile
        fields = ['photo', 'first_name', 'last_name', 'account_type', 'facebook_url', 'website_url', 'about']