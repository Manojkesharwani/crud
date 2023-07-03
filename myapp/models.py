from django.db import models
from django.conf import settings
from django.utils import timezone




class MYBLOGAPP(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    Designation=models.CharField(max_length=50)
    create_date=models.DateTimeField()


    
    def __str__(self):
        return self.name

