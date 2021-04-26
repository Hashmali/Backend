from django.db import models
from api.project.models import Project

class Expense(models.Model):
    amount=models.IntegerField()
    description=models.TextField()
    month=models.DateField(blank=True,null=True)


class Income(models.Model):
    amount=models.IntegerField()
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    month=models.DateField()
    image=models.URLField(default="")