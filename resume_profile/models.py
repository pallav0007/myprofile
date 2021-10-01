from django.db import models

# Create your models here.
class Bio(models.Model):
    bio=models.TextField(max_length=5000,default="Hi there")
class Information(models.Model):
    fieldname=models.CharField(max_length=200)
    description=models.CharField(max_length=500,default="information not added")


    def __str__(self):
        return self.fieldname
