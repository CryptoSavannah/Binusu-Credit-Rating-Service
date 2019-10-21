from django.contrib import admin

from .models import Loans, CreditScores, LendingRank

admin.site.register(Loans)
admin.site.register(CreditScores)
admin.site.register(LendingRank)

