import sys
import json
import re

from accounts.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from accounts.serializers import TokenSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .helpers import hash_input, random_string_digits

from .serializers import CreateUserSerializer, GetUserCreateSerializer, UserCreateFormSerializer, UserDetailSerializer


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)

            user_data = UserDetailSerializer(user)

            token_serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            token_serializer.is_valid()
            data_dict = {"status":200, "data": {"token":token_serializer.data, "user_details":user_data.data}}
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response({"status":404, "error":"username or password incorrect"}, status=status.HTTP_404_NOT_FOUND)

class RegisterView(generics.CreateAPIView):
    """
    POST auth/register/
    """

    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    def post(self,request, *args, **kwargs):

        serializer = UserCreateFormSerializer(data=request.data)
        if serializer.is_valid():

            user_data = {
                'username':random_string_digits(),
                'first_name':serializer.data['first_name'],
                'last_name':serializer.data['last_name'],
                'email':'email@email.com',
                'password':serializer.data['password'],
                'hashed_nin':hash_input(serializer.data['nin_number']),
                'bnu_address':hash_input(serializer.data['nin_number']),
                'physical_address':serializer.data['physical_address'],
                'refferal_id':serializer.data['refferal_id'],
                'role':serializer.data['role'],
            }

            client_data = CreateUserSerializer(data=user_data)
            client_data.is_valid(raise_exception=True)
            client_data.save()

            data_dict = {"status":201, "data":{"user_details":client_data.data}}
            return Response(data_dict, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
