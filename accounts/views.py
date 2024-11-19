from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend

from accounts.serializers import (
    UserSerializer,
    UserLoginSerializer,
)

User = get_user_model()


class SignInView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(email=email, password=password)

            if user:
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    user_details = {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "is_superuser": user.is_superuser,
                        "reference": user.reference,
                        "slug": user.slug,
                        "last_login": user.last_login,
                        "token": token.key,
                        "is_manager": user.is_manager,
                        "is_accountant": user.is_accountant,
                    }
                    return Response(user_details, status=status.HTTP_200_OK)
                else:
                    return Response(
                        {"detail": ("User account is disabled.")},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"detail": ("Unable to log in with provided credentials.")},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(
            {"message": "User logged out successfully"},
            status=status.HTTP_200_OK,
        )


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_accountant", "is_manager"]
