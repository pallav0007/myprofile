from django.db import models

# Create your models here.
class myskills(models.Model):
    name=models.CharField(max_length=200)
    about=models.TextField(max_length=5000)