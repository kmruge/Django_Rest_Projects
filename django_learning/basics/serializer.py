from rest_framework import serializers
from .models import fieldsLearning1

def age1_validator(value):
    if value == 20:
        raise serializers.ValidationError("Age should not be 20 validator")

def age2_validator(value):
    if value == 30:
        raise serializers.ValidationError("Age should not be 30 validator")
class profileSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=200)
    age=serializers.IntegerField(min_value=18, max_value=100, error_messages={
        'min_value':'Age should be greater than 18 custom',
        'max_value':'Age should be less than 100 custom'

        }, validators=[age1_validator, age2_validator])
    address=serializers.CharField(max_length=200,initial="Bangalore")
    email=serializers.CharField(max_length=50)
    phone=serializers.IntegerField()
    run=serializers.CharField(max_length=200, read_only=True)
    personal_number=serializers.IntegerField()

    def validate_name(self, value):
        if fieldsLearning1.objects.filter(name=value).exists():
            raise serializers.ValidationError("Name already exists")
        return value


    def create(self, validated_data):
        return fieldsLearning1.objects.create(**validated_data)

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
        model=fieldsLearning1
        fields='__all__'

class EntrySerializer(serializers.Serializer):
    blog=serializers.CharField(source='blog.name')
    headline=serializers.CharField()
    body_text=serializers.CharField()
    authors=serializers.CharField(source='basics.Authors.name')
    pub_date=serializers.DateField()
    rationg=serializers.IntegerField()