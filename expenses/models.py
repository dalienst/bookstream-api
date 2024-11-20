from django.db import models
from django.contrib.auth import get_user_model

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel
from categories.models import Category
from business.models import Business

User = get_user_model()


class Expense(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_expenses"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="business_expenses"
    )

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user.email} - {self.category.name} - {self.amount}"
