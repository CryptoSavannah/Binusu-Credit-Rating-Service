from django.db import models

class Loans(models.Model):
    borrower_address        = models.CharField(max_length=108)
    lending_address         = models.CharField(max_length=108, null=True, blank=True)
    borrower_nin_hash       = models.CharField(max_length=64, null=True, blank=True)
    pay_id                  = models.CharField(max_length=64, null=True, blank=True)
    loan_amount             = models.DecimalField(max_digits=20, decimal_places=2)
    expected_amount         = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    outstanding_amount      = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    expected_payment_date   = models.DateField(auto_now_add=False)
    loan_status             = models.IntegerField() 
    date_requested          = models.DateField(auto_now_add=True)
    date_approved           = models.DateField(auto_now_add=False, null=True, blank=True)
    actual_payment_date     = models.DateField(auto_now_add=False, null=True, blank=True)

class LoanPayments(models.Model):
    loan_id                 = models.ForeignKey(Loans, on_delete=models.CASCADE, related_name="related_loan")
    installment_amount      = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    paying_address          = models.CharField(max_length=108)
    date_paid               = models.DateTimeField(auto_now_add=True)
    installment_number      = models.IntegerField()
    repayment_penalty       = models.BooleanField(default=False)
    penalty_amount          = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)

class CreditScores(models.Model):
    score_owner_address             = models.CharField(max_length=108)
    credit_refferal                 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    network_contribution            = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    new_credit                      = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)   
    loan_frequency                  = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    initial_repayment_installment   = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    average_number_of_installments  = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    loan_completion                 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    late_payment_penalties          = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    final_score                     = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_computed                   = models.DateTimeField(auto_now_add=True)