from rest_framework import serializers

from business.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, source="user.email")
    logo = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Business
        fields = (
            "id",
            "user",
            "name",
            "description",
            "logo",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.logo = validated_data.get("logo", instance.logo)
        instance.save()
        return instance
