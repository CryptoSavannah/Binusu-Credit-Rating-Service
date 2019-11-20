from rest_framework import serializers
from .models import Loans, LoanPayments, ScoreMetric
from accounts.models import User

class LoansRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Loans
        fields = ('id', 'borrower_address', 'lending_address', 'borrower_nin_hash', 'pay_id', 'loan_amount', 'loan_status', 'date_requested', 'date_approved', 'actual_payment_date', 'expected_amount', 'expected_payment_date', 'outstanding_amount')

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
    loan_id         = serializers.CharField(max_length=10)
    status          = serializers.CharField(max_length=2)
    lending_address = serializers.CharField(max_length=255)  
    pay_id          = serializers.CharField(max_length=255) 

class LoanRepaymentSerializer(serializers.Serializer):
    loan_id         = serializers.CharField(max_length=10)
    paying_address  = serializers.CharField(max_length=255)  
    amount          = serializers.CharField(max_length=255)  

class LoanRepaymentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanPayments
        fields = ('loan_id', 'installment_amount', 'paying_address', 'installment_number') 

class IdSerializer(serializers.Serializer):
    loan_id         = serializers.CharField(max_length=10)

class LoanPaymentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanPayments
        fields = ('loan_id', 'installment_amount', 'paying_address', 'installment_number', 'date_paid', 'repayment_penalty') 

class ScoreMetricSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreMetric
        fields = ('metric_title', 'metric_percentage_contribution', 'metric_description', 'metric_classification')