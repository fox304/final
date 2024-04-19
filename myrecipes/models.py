from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    steps = models.TextField()
    time_minutes = models.IntegerField()
    image = models.ImageField(upload_to='pictures')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', null=True, )

    class Meta:
        """прверка названия блюда на уникальность"""
        unique_together = ('name',)

    def __str__(self):
        return f'{self.name}, {self.description}'

    def get_absolute_url(self):
        return reverse('browse', kwargs={'recipe_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
