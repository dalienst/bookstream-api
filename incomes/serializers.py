from rest_framework import serializers

from categories.models import Category
from incomes.models import Income


class IncomeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)
    category = serializers.SlugRelatedField(
        slug_field="reference", queryset=Category.objects.all()
    )
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()

    class Meta:
        model = Income
        fields = (
            "id",
            "user",
            "category",
            "amount",
            "date",
            "description",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
