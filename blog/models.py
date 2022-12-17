from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE);

    def __str__(self):
        return self.title


class BuyTyr(models.Model):
    title1 = models.CharField(max_length=200)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE);

    def __str__(self):
        return self.title1


class Comments(models.Model):
    name = models.CharField(max_length=100)
    comments = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comments[:60]





