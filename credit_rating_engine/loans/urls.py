from django.urls import path, include
from .views import BorrowersLoanList, BorrowerLoanRequestList

urlpatterns = [
    path('loans/', BorrowersLoanList.as_view(), name="loans-endpoint"),
    path('loans/requests/', BorrowerLoanRequestList.as_view(), name="loans-requests-lists-endpoint"),
]