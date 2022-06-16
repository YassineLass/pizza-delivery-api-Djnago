from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=50)
    phone_number = PhoneNumberField(allow_null=False,allow_blank=False)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username','email','phone_number','password','password2']

    def validate(self,attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail="Username already exists")    
        email_exists = User.objects.filter(username=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="Email already exists")    
        phonenumber_exists = User.objects.filter(username=attrs['phone_number']).exists()
        if phonenumber_exists:
            raise serializers.ValidationError(detail="Phone number already exists")  
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})           
        
        return super().validate(attrs)
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)      