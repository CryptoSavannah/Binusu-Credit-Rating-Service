from django.db import models

class User(models.Model):
    full_name               = models.CharField(max_length=255)
    hashed_nin              = models.CharField(max_length=64, unique=True)
    bnu_address             = models.CharField(max_length=108)
    physical_address        = models.CharField(max_length=255)
    user_number             = models.CharField(max_length=255)
    password                = models.CharField(max_length=255)
    refferal_id             = models.CharField(max_length=6)
    role                    = models.IntegerField()

    class Meta:
        unique_together = ['hashed_nin', 'user_number']


class Loans(models.Model):
    borrower_address        = models.CharField(max_length=108)
    lending_address         = models.CharField(max_length=108, null=True, blank=True)
    borrower_nin_hash       = models.CharField(max_length=64, null=True, blank=True)
    pay_id                  = models.CharField(max_length=64, null=True, blank=True)
    loan_amount             = models.DecimalField(max_digits=20, decimal_places=2)
    expected_payment_date   = models.DateField(auto_now_add=False)
    loan_status             = models.IntegerField() 
    date_requested          = models.DateField(auto_now_add=True)
    date_approved           = models.DateField(auto_now_add=False, null=True, blank=True)
    actual_payment_date     = models.DateField(auto_now_add=False, null=True, blank=True)

class LoanPayments(models.Model):
    loan_id                 = models.ForeignKey(Loans, on_delete=models.CASCADE, related_name="related_loan")
    paying_address          = models.CharField(max_length=108)
    date_paid               = models.DateTimeField(auto_now_add=True)
    installment_number      = models.IntegerField()
    repayment_penalty       = models.BooleanField(default=False)
    penalty_amount          = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)