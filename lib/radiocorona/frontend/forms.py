from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import Submission
from radiocorona.users.models import RedditUser
from radiocorona.frontend.models import Category

from captcha.fields import ReCaptchaField

categories = Category.objects.all()

class UserForm(forms.ModelForm):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]*$',
                                  'This value may contain only letters, '
                                  'numbers and _ characters.')
    username = forms.CharField(widget=forms.TextInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Username",
         'required': '',
         'autofocus': ''}),
        max_length=12,
        min_length=3,
        required=True,
        validators=[alphanumeric])
    password = forms.CharField(widget=forms.PasswordInput(
        attrs=
        {'class': "form-control",
         'placeholder': "Password",
         'required': ''}),
        min_length=4,
        required=True)

    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'password', 'captcha')


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "first_name",
               'type': "text"}),
        min_length=1,
        max_length=12,
        required=False
    )

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "last_name",
               'type': "text"}),
        min_length=1,
        max_length=12,
        required=False
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control",
               'id': "email",
               'type': "text"}),
        required=False
    )

    display_picture = forms.BooleanField(required=False)

    about_text = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control",
               'id': "about_me",
               'rows': "4",
               }),
        max_length=500,
        required=False
    )

    homepage = forms.CharField(widget=forms.URLInput(
        attrs={'class': "form-control",
               'id': "homepage"}),
        required=False
    )

    github = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "github",
               'type': "text"}),
        required=False,
        max_length=39
    )

    twitter = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "twitter",
               'type': "text"}),
        required=False,
        max_length=15
    )

    class Meta:
        model = RedditUser
        fields = ('first_name', 'last_name', 'email',
                  'display_picture', 'about_text',
                  'homepage', 'github', 'twitter')


class SubmissionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'placeholder': "Submission title"}),
        required=True, min_length=1, max_length=250)

    #url = forms.URLField(widget=forms.URLInput(
    #    attrs={'class': "form-control",
    #           'placeholder': "(Optional) http:///www.example.com"}),
    #    required=False)

    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'rows': "3",
            'placeholder': "What's happening?"}),
        max_length=5000,
        required=False)

    image = forms.ImageField(required=False)

    category = forms.ModelChoiceField(queryset=categories, required=False)

    class Meta:
        model = Submission
        fields = ('title', 'text', 'image', 'category')
