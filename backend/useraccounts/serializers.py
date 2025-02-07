from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, UserProfile


# 1. CustomUserSerializer (for User Model)
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'is_verified', 'is_active', 'is_staff', 'created_at', 'updated_at']


# 2. UserProfileSerializer (for UserProfile Model)
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'website', 'location', 'twitter', 'github', 'linkedin', 'created_at', 'updated_at']


# 3. RegisterSerializer (for User Registration)
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords must match.")

        return attrs

    def create(self, validated_data):
        # Remove 'password2' from the validated_data before creating the user
        validated_data.pop('password2', None)

        password = validated_data.pop('password')  # Pop password field
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)  # Set the password securely
        user.save()
        return user



# 4. LoginSerializer (for User Login)
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # Validate credentials for login
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)  # Authenticate user using email and password
        if not user or not user.is_active:
            raise serializers.ValidationError("Invalid credentials or inactive user.")
        
        attrs['user'] = user  # Add the user object to the attributes to be used later
        return attrs


# 5. UserProfileUpdateSerializer (for updating User Profile)
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'website', 'location', 'twitter', 'github', 'linkedin']  # Profile fields to be updated
