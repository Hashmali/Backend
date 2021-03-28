from django.db import models
from api.worker.models import User
from api.project.models import Project

class Mission(models.Model):
    worker=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    date=models.DateField()
    description=models.TextField()


    def __str__(self):
        return data+worker



