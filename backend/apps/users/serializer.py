from rest_framework import serializers
from .models import CustomUser
from django.core.validators import RegexValidator

class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(regex=r'^\d{10}$', message="Must be 10 digits.")
        ]
    )
    password = serializers.CharField(write_only=True, required=True, min_length=7)

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password', 'user_type', 'phone_number']

    def create(self, validated_data):
        print("Step 3: Inside create() - received validated_data =>", validated_data)
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    
       