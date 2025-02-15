from django.db import models 

class Student(models.Model):
    name = models.CharField(max_length=55)
    email=models.EmailField(unique=True)
    age=models.IntegerField()