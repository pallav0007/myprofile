from django.db import models

# Create your models here.
class myprojects(models.Model):
    domain=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    tech=models.TextField(max_length=5000,default="not specified")
    about=models.TextField(max_length=5000)
    url=models.CharField(max_length=500)

    def __str__(self):
        return self.name

