from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from business.serializers import BusinessSerializer
from business.models import Business


class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = BusinessSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Business.objects.filter(user=self.request.user)
