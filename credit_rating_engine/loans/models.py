from django.db import models

class Loans(models.Model):
    borrower_address        = models.CharField(max_length=255)
    lending_address         = models.CharField(max_length=255)
    borrower_nin_hash       = models.CharField(max_length=255)
    pay_id                  = models.CharField(max_length=255)
    loan_amount             = models.DecimalField(max_digits=2)
    expected_payment_date   = models.DateTimeField(auto_now_add=False)
    loan_status             = models.IntegerField()
    date_requested          = models.DateTimeField(auto_now_add=True)
    date_approved           = models.DateTimeField(auto_now_add=False)
    actual_payment_date     = models.DateTimeField(auto_now_add=False)

class LoanPayments(models.Model):
    loan_id                 = models.ForeignKey(Loans, on_delete=models.CASCADE, related_name="related_loan")
    paying_address          = models.CharField(max_length=255)
    date_paid               = models.DateTimeField(auto_now_add=True)
    installment_number      = models.IntegerField()
    repayment_penalty       = models.BooleanField(default=False)
    penalty_amount          = models.DecimalField(max_digits=2, blank=True, null=True)

