from rest_framework import serializers
from .models import person, color
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model=color
        fields=["id","Color"]


class personSerializers(serializers.ModelSerializer):
    #Name should same as Column name in the model class
    Color=colorSerializer()
    Relation=serializers.SerializerMethodField()

    class Meta:
        model=person
        fields='__all__'

        #When we use ForeignKey in model.ph, it list the id instead of value. In order to send data along with id we will use depth.
        # depth=1

        # validate used to valid specific data that we pass into this serialiser class(Take all data)
    def validate(self, data1):
        if len(data1['Name'])<5:
            raise serializers.ValidationError("Name should be more than 5 character")
        return data1
        
        #We can write validate_(Data_Field_Name) which takes only field data we mentioned.
    
    def get_Relation(self,obj):
        color_name=color.objects.get(id=3)
        return {"Color_Name":obj.Name,"Address_Name":"India"}


    def validate_Age(self,data):
        if data<18:
            raise serializers.ValidationError("Age should be more than 18")
        return data
    
    def validate_Address(self,address):
        if len(address)<6:
            raise serializers.ValidationError("Address must be more than 6 character")
        return address
    
class RegisterUser(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    def validate(self, attrs):
        if attrs['username']:
            if User.objects.filter(username=attrs['username']).exists():
                raise serializers.ValidationError("User Name has taken")
        return attrs
    
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class passwordChangeSerializer(serializers.Serializer):
    username=serializers.CharField()
    oldpassword=serializers.CharField()
    newpassword=serializers.CharField()
        
    def validate(self,data):
        if User.objects.filter(username=data['username']).exists():
            user=User.objects.get(username=data['username'])
            user.check_password(data['oldpassword'])
            return data
        
    def update(self,validated_data):
        user=authenticate(username=validated_data['username'],password=validated_data['oldpassword'])
        if not user:
            raise serializers.ValidationError('Invalid Password')
        # user=User.objects.get(username=data['username'])
        user.set_password(validated_data['newpassword'])
        user.save()


class LogInAuthSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()