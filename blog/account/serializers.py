from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class AccountSerializer(serializers.Serializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, attrs):
        user=User.objects.filter(username=attrs['username'].lower()).exists()
        if user:
            raise serializers.ValidationError("Username is already taken")
        return attrs
    
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'].lower(), 
                                 first_name=validated_data['first_name'], 
                                 last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

class loginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def get_jwt_token(self,data):
        user=authenticate(username=data['username'],password=data['password'])
        if not user:
            raise serializers.ValidationError("User name doesn't exist")
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

