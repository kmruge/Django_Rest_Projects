from django.db import models

# Create your models here.

class color(models.Model):
    Color=models.CharField(max_length=100)
    Color_code=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.Color

class person(models.Model):
    Name=models.CharField(max_length=200)
    Age=models.IntegerField()
    Address=models.CharField(max_length=200)
    Color=models.ForeignKey(color,on_delete=models.CASCADE,related_name='color',null=True,blank=True)
    
    def __str__(self):
        return self.Name