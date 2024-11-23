from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from categories.models import Category
from expenses.serializers import ExpenseSerializer
from incomes.serializers import IncomeSerializer


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)
    name = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=Category.objects.all())]
    )
    category_expenses = ExpenseSerializer(many=True, read_only=True)
    category_incomes = IncomeSerializer(many=True, read_only=True)

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
            "category_expenses",
            "category_incomes",
        )
