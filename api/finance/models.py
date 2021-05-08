from django.db import models
from api.project.models import Project

class Expense(models.Model):
    title=models.CharField(max_length=100,default="title")
    amount=models.IntegerField()
    description=models.TextField()
    month=models.DateField(blank=True,null=True)


class Income(models.Model):
    title=models.CharField(max_length=100,default="title")
    amount=models.IntegerField()
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    month=models.DateField()
    image=models.URLField(default="")