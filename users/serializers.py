from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'phone_no',
            'role',
            'preferred_language',
            'password',
        ]

    def create(self , validated_data):
        password = validated_data.pop('password')

        user=User(**validated_data)
        user.set_password(password)
        user.save()

        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self , data):
        user = authenticate(username=data["username"] , password=data["password"])

        if not user:
            raise serializers.ValidationError("Invalid ceredials")
        
        data["user"] = user

        return data
    



