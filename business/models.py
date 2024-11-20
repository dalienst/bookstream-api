from django.db import models
from django.contrib.auth import get_user_model

from accounts.abstracts import TimeStampedModel, ReferenceSlugModel, UniversalIdModel
from cloudinary.models import CloudinaryField

User = get_user_model()


class Business(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="business")
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = CloudinaryField("logos", blank=True, null=True)

    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.user.email
