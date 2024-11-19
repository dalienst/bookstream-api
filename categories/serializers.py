from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "user",
            "name",
            "description",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
