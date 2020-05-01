from django.db import models
from django.utils import timezone
import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

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
