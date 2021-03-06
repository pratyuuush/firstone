from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Post, Rating, Comment
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
        

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username","first_name", "last_name",
                  "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ("bio", "ac_type", "address1", "address2", "city", "state", "country", "zip_code", "phone")

class SettingsUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SettingsUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        'post_something',
        'post_type',
        ]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        'post_something',
        'post_type'
        ]        

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
        'comment',
        'rate_type',
        ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']      