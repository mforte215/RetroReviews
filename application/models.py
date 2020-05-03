from django.db import models
from django.utils import timezone
import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from django.conf import settings

# Create your models here.



class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Article(models.Model):
    title_text = models.CharField(max_length=100, null=True)
    article_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    header_image = models.ImageField(upload_to='images/', null=True)
    article_body_text = RichTextField()
    article_author = models.CharField(max_length=100, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    active = models.BooleanField(default=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.id, self.created_by)

    class Meta:
        ordering = ['created_on']


    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class Reply(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies", null=True)
    text = models.TextField(max_length=1000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Reply {} by {}'.format(self.id, self.created_by)


    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class UpVotes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    vote_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.vote_text

class VideoLink(models.Model):
    video_title = models.CharField(max_length=100, null=True)
    video_url = models.CharField(max_length=100, null=True)
    pub_date = models.DateTimeField('date published', null=True)
