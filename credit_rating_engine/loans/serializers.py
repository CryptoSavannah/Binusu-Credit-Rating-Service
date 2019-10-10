from rest_framework import serializers
from .models import Loans, LoanPayments
from accounts.models import User

class LoansRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Loans
        fields = ('id', 'borrower_address', 'lending_address', 'borrower_nin_hash', 'pay_id', 'loan_amount', 'loan_status', 'date_requested', 'date_approved', 'actual_payment_date', 'expected_amount', 'expected_payment_date')

class LoanPaymentsRetrieveSerializer(serializers.ModelSerializer):
    pass

class LoansFormSerializer(serializers.Serializer):
    """
    Loans Form serializer
    """
    borrowers_address      = serializers.CharField(max_length=255)
    loan_amount            = serializers.CharField(max_length=255)
    expected_amount        = serializers.CharField(max_length=255)
    repayment_date         = serializers.CharField(max_length=255)
    borrower_nin_hash      = serializers.CharField(max_length=255)

class LoansCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loans
        fields = ('id', 'borrower_address', 'borrower_nin_hash', 'loan_amount', 'expected_payment_date', 'loan_status', 'expected_amount')

class LoanRequestSerializer(serializers.Serializer):
    address      = serializers.CharField(max_length=255)
    

class SpendKeySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('spendp_key', 'spendpr_key')

class LoanIdSerializer(serializers.Serializer):
    loan_id      = serializers.CharField(max_length=10)
    status       = serializers.CharField(max_length=2)   