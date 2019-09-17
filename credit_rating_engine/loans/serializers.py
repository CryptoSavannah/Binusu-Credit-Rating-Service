from rest_framework import serializers
from .models import Loans, LoanPayments

class LoansRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Loans
        fields = ('borrower_address', 'lending_address', 'borrower_nin_hash', 'pay_id', 'loan_amount')

class LoanPaymentsRetrieveSerializer(serializers.ModelSerializer):
    pass