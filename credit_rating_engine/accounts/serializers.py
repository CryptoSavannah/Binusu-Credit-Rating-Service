from rest_framework import serializers
from accounts.models import User

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

class UserCreateFormSerializer(serializers.Serializer):
    first_name            = serializers.CharField(max_length=255)
    last_name             = serializers.CharField(max_length=255)  
    nin_number            = serializers.CharField(max_length=255)
    physical_address      = serializers.CharField(max_length=255)
    password              = serializers.CharField(max_length=255)
    refferal_id           = serializers.CharField(max_length=255)
    role                  = serializers.IntegerField()

class CreateUserSerializer(serializers.ModelSerializer):
    """
    This serializer exposes fields to create a user
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'password', 'hashed_nin', 'bnu_address', 'spendp_key', 'spendpr_key','physical_address', 'refferal_id', 'role')

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class GetUserCreateSerializer(serializers.Serializer):
    """
    This serializer exposes fields to create a user
    """
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    role = serializers.CharField(max_length=255)
    wallet_pin = serializers.CharField(max_length=255)

    def validate_wallet_pin(self, value):
        if len(value) != 5:
           raise serializers.ValidationError("Wallet pin should be 5 digits long")
        return value 


class UserDetailSerializer(serializers.ModelSerializer):
    """
    This serializer return user details
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'hashed_nin', 'bnu_address', 'physical_address', 'refferal_id')