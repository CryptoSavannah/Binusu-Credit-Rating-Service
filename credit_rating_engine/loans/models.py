from django.db import models
from accounts.models import User

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

class LendingRank(models.Model):
    rank_owner_address              = models.CharField(max_length=108)
    number_of_loans_monthly         = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    amount_lent_monthly             = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    final_score                     = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_computed                   = models.DateTimeField(auto_now_add=True)

class ScoreMetric(models.Model):
    metric_title                    = models.CharField(max_length=255)
    metric_percentage_contribution  = models.DecimalField(max_digits=5, decimal_places=2)
    metric_description              = models.TextField()
    metric_classification           = models.CharField(max_length=15)
    date_added                      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.metric_title)

class CreditScoreCalculation(models.Model):
    related_address       = models.ForeignKey(User, on_delete=models.CASCADE, related_name="score_owner")
    related_metric        = models.ForeignKey(ScoreMetric, on_delete=models.CASCADE, related_name="metric_id")          
    metric_score          = models.IntegerField()  
    date_computed         = models.DateTimeField(auto_now_add=True)  