from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
# Create your models here.
class postbase(models.Model):
    # UUID=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    """auto_now_add for the creation time and auto_now for the last update time:"""
    # id=models.IntegerField(primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True, db_index=True)

    class Meta:
        abstract=True

class blog(postbase):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=2000)
    image=models.ImageField()