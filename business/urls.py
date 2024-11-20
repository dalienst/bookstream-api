from django.urls import path

from business.views import BusinessDetailView

urlpatterns = [
    path("<str:slug>/", BusinessDetailView.as_view(), name="business_detail"),
]
