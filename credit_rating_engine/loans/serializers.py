from rest_framework import serializers
from .models import User ,Loans, LoanPayments

class UserFormSerializer(serializers.Serializer):
    """
    User form serializer
    """
    full_name             = serializers.CharField(max_length=255)
    nin_number            = serializers.CharField(max_length=255)
    physical_address      = serializers.CharField(max_length=255)
    password              = serializers.CharField(max_length=255)

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('full_name', 'hashed_nin', 'bnu_address', 'physical_address', 'user_nunber', 'password', 'refferal_id', 'role')

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('user_number', 'password')

class LoansRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Loans
        fields = ('id', 'borrower_address', 'lending_address', 'borrower_nin_hash', 'pay_id', 'loan_amount')

class LoanPaymentsRetrieveSerializer(serializers.ModelSerializer):
    pass

class LoansFormSerializer(serializers.Serializer):
    """
    Loans Form serializer
    """
    borrowers_address      = serializers.CharField(max_length=255)
    loan_amount            = serializers.CharField(max_length=255)
    repayment_date         = serializers.CharField(max_length=255)
    borrower_nin_hash      = serializers.CharField(max_length=255)

class LoansCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loans
        fields = ('borrower_address', 'borrower_nin_hash', 'loan_amount', 'expected_payment_date', 'loan_status')