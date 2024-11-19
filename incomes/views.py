from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from incomes.serializers import IncomeSerializer
from incomes.models import Income


class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "category"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "category"]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
