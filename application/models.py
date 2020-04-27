from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Article(models.Model):
    title_text = models.CharField(max_length=100, null=True)
    article_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    header_image = models.ImageField(upload_to='images/', null=True)

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