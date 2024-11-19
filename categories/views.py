from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend

from categories.serializers import (
    CategorySerializer,
)
from categories.models import Category


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "slug"

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
