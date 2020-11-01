from django import forms
from taggit.forms import TagWidget
from tinymce.widgets import TinyMCE

from ads.models import Ad


class AdForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        max_length=120,
        help_text="Max 120 characters",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}),
        required=True,
    )

    image = forms.ImageField(
        label="Photo",
        help_text="We accept jpg, png, etc.",
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control form-control pr-3 shadow p-1 mb-1 bg-white rounded"}), required=False,
    )

    short_description = forms.CharField(
        label="Short description",
        max_length=300,
        help_text="Add short description of your problem.",
        widget=forms.Textarea(attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}),
        required=True,

    )

    long_description = forms.CharField(
        label="Long description",
        max_length=1500,
        help_text="Give us more details about your problem",
        widget=TinyMCE(attrs={}),
        required=True,
    )

    class Meta:
        model = Ad
        fields = ('title', 'image', 'tags', 'short_description', 'long_description')
        widgets = {
            'tags': TagWidget(attrs={"class": "form-control form-control-lg pr-5 shadow p-1 mb-1 bg-white rounded"}),
        }
