from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.validators import (
    validate_password_digit,
    validate_password_uppercase,
    validate_password_lowercase,
    validate_password_symbol,
)
from business.models import Business
from business.serializers import BusinessSerializer

User = get_user_model()


class BaseUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        max_length=128,
        min_length=5,
        write_only=True,
        validators=[
            validate_password_digit,
            validate_password_uppercase,
            validate_password_symbol,
            validate_password_lowercase,
        ],
    )
    avatar = serializers.ImageField(use_url=True, required=False)
    business = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "avatar",
            "reference",
            "slug",
            "is_staff",
            "is_active",
            "is_manager",
            "is_accountant",
            "created_at",
            "updated_at",
            "business",
        )

    def create(self, validated_data, role_field=None):
        try:
            user = User.objects.create_user(
                email=validated_data["email"],
                password=validated_data["password"],
                first_name=validated_data.get("first_name", ""),
                last_name=validated_data.get("last_name", ""),
                avatar=validated_data.get("avatar", None),
            )
            if role_field:
                setattr(user, role_field, True)
            user.save()
            Business.objects.create(user=user)
            return user
        except Exception as e:
            raise serializers.ValidationError(f"User creation failed: {str(e)}")

    def get_business(self, obj):
        business = obj.business.all()
        serializers = BusinessSerializer(business, many=True)
        return serializers.data


class UserSerializer(BaseUserSerializer):

    def create(self, validated_data):
        return super().create(validated_data, role_field="is_manager")


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
