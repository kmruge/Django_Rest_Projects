from rest_framework import serializers
from .models import fieldsLearning

class profileSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=200)
    age=serializers.IntegerField()
    address=serializers.CharField(max_length=200)
    email=serializers.CharField(max_length=50)
    phone=serializers.IntegerField()
    personal_number=serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        return fieldsLearning.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.address=validated_data.get('address',instance.address)
        instance.email=validated_data.get('email',instance.email)
        instance.phone=validated_data.get('phone',instance.phone)
        instance.personal_number=validated_data.get('personal_number',instance.personal_number)
        instance.save()
        return instance

class profileSerializerModel(serializers.ModelSerializer):
    created_at=serializers.DateTimeField(read_only=True)
    personal_number=serializers.IntegerField(write_only=True)
    check=serializers.CharField(required=True)
    class Meta:
        model=fieldsLearning
        fields='__all__'
    