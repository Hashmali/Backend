from django.db import models
from api.worker.models import User
from api.project.models import Project

class Mission(models.Model):
    title=models.CharField(max_length=100,null=True,blank=False)
    worker=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    date=models.DateField()
    description=models.TextField()


    def __str__(self):
        return self.title



