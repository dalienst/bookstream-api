from django.db import models
from django.contrib.auth import get_user_model

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel
from categories.models import Category
from business.models import Business

User = get_user_model()


class Income(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_incomes"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="business_incomes"
    )

    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user.email} - {self.category.name} - {self.amount}"
