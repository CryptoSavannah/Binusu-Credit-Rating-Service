from django.contrib import admin

from .models import Loans, LendingRank, ScoreMetric, CreditScoreCalculation

admin.site.register(Loans)
admin.site.register(ScoreMetric)
admin.site.register(LendingRank)
admin.site.register(CreditScoreCalculation)

