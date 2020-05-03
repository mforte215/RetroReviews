from django.contrib import admin

from application.models import Article, VideoLink, CustomUser, Comment, Reply

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from application.forms import CustomUserCreationForm, CustomUserChangeForm


class ReplyInline(admin.TabularInline):
    model = Reply

class CommentInline(admin.TabularInline):
    model = Comment

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'text', 'created_on', 'active')
    list_filter = ('active', 'created_on', 'created_by')
    search_fields = ('name', 'text', 'created_by')
    actions = ['disable_comments']
    readonly_fields = ["created_by", "text", "created_on", "article"]

    inlines = [
            ReplyInline,
        ]

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

class ReplyAdmin(admin.ModelAdmin):
    model = Reply


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(VideoLink)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
