from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Comment
from django.forms import ModelForm, Textarea
import logging


logger = logging.getLogger("mylogger")

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
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':3, 'cols':115, 'style':'width: 90%; resize:none;'}))
    parent_id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    
    def clean_parent_id(self):
        parent_id = self.cleaned_data['parent_id']
        logger.info("-------------------------------")
        logger.info("Logging parent id from forms:")
        logger.info(parent_id)
        logger.info("-------------------------------")

    class Meta:
        model = Comment
        fields= ('text',)

