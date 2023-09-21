from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class postbase(models.Model):
    UUID=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract=True

class post(postbase):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=2000)
    image=models.ImageField()