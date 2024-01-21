from django.db import models

# Create your models here.
class blood(models.Model):
    blood_name=models.CharField(max_length=20)

class profile(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    blood=models.ForeignKey(blood, on_delete=models.CASCADE, related_name='bloodgroup')