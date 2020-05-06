from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Comment
from django.forms import ModelForm, Textarea

class CustomUserCreationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_number' )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_number' )

class CommentForm(ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':3, 'cols':115, 'style':'resize:none;'}))

    class Meta:
        model = Comment
        fields= ('text',)

