from django.db import models
from django.contrib.auth.models import User


# Many to One
# Many to Many
# One to Many
# each article has one author
# User -> DELETE we use on_delete to remove all article of this user
# we can use set.null for important things

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
