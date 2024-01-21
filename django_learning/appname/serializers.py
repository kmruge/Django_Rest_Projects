from rest_framework import serializers
from appname.models import profile, blood

class bloodSerializer(serializers.ModelSerializer):
    class Meta:
        model=blood
        exclude=['id']

class profileSerializer(serializers.ModelSerializer):
    blood=bloodSerializer()
    class Meta:
        model=profile
        fields='__all__'