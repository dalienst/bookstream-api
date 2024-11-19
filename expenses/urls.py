from django.urls import path

from categories.views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("", CategoryListCreateView.as_view(), name="category_list"),
    path("<str:slug>/", CategoryDetailView.as_view(), name="category_detail"),
]
