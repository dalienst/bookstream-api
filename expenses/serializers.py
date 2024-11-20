from rest_framework import serializers

from categories.models import Category
from expenses.models import Expense
from business.models import Business


class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)
    category = serializers.SlugRelatedField(
        slug_field="reference", queryset=Category.objects.all()
    )
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()
    business = serializers.SlugRelatedField(
        slug_field="reference", queryset=Business.objects.all()
    )

    class Meta:
        model = Expense
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
            "business",
        )
