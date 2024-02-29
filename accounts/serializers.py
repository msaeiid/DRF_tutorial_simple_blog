from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from accounts.models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, attrs):
        email_exists = User.object.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("Email already registered")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
