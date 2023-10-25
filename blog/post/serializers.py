
from rest_framework import serializers
from .models import blog
class postSerializers(serializers.ModelSerializer):
    class Meta:
        model=blog
        fields='__all__'