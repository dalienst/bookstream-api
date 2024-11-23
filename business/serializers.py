from rest_framework import serializers

from business.models import Business
from incomes.serializers import IncomeSerializer
from expenses.serializers import ExpenseSerializer


class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, source="user.email")
    logo = serializers.ImageField(use_url=True, required=False)
    business_incomes = serializers.SerializerMethodField()
    business_expenses = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = (
            "id",
            "user",
            "name",
            "description",
            "logo",
            "location",
            "phone",
            "currency",
            "fiscal_year",
            "email",
            "is_compliant",
            "registration_number",
            "vat_number",
            "created_at",
            "updated_at",
            "slug",
            "reference",
            "business_incomes",
            "business_expenses",
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.description = validated_data.get("description", instance.description)
        instance.logo = validated_data.get("logo", instance.logo)
        instance.location = validated_data.get("location", instance.location)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.currency = validated_data.get("currency", instance.currency)
        instance.fiscal_year = validated_data.get("fiscal_year", instance.fiscal_year)
        instance.is_compliant = validated_data.get("is_compliant", instance.is_compliant)
        instance.registration_number = validated_data.get(
            "registration_number", instance.registration_number
        )
        instance.vat_number = validated_data.get("vat_number", instance.vat_number)
        instance.save()
        return instance

    def get_business_incomes(self, obj):
        business_incomes = obj.business_incomes.all()
        serializers = IncomeSerializer(business_incomes, many=True)
        return serializers.data

    def get_business_expenses(self, obj):
        business_expenses = obj.business_expenses.all()
        serializers = ExpenseSerializer(business_expenses, many=True)
        return serializers.data
