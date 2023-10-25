from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
def EmailValidator(value):
    if '@' not in value:
        raise ValidationError("Email should contain @")

class fieldsLearning(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(100)])
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=50,validators=[EmailValidator])
    phone=models.IntegerField()
    personal_number=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        db_table="fieldsLearning-1"