from django.contrib import admin

from application.models import Article, VideoLink, CustomUser

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from application.forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)
admin.site.register(VideoLink)
