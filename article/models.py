from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """文章分类"""
    tittle = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.tittle


class Article(models.Model):
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL,related_name='articles')
    tittle = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='articles')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.tittle
