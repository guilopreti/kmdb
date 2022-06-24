from django.contrib.auth import authenticate
from django.shortcuts import get_list_or_404
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response, status

from .models import User
from .permissions import UserPermission
from .serializers import LoginSerializer, UserSerializer


# Create your views here.
class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED
        )


class UserView(APIView, PageNumberPagination):
    permission_classes = [UserPermission]

    def get(self, request):
        users = get_list_or_404(User)

        result_page = self.paginate_queryset(users, request, view=self)

        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class UserParamsView(APIView):
    permission_classes = [UserPermission]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

            serializer = UserSerializer(user)

            return Response(serializer.data)
        except:
            return Response(
                {"message": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
