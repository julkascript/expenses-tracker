from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField(blank=False)


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(blank=False)
    description = models.TextField(blank=False)
    price = models.FloatField(blank=False)
