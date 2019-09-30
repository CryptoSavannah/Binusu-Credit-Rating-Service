from django.urls import path, include
from .views import BorrowersLoanList, BorrowerLoanRequestList, LoansDetail, TransactionHistory

urlpatterns = [
    path('loans/', BorrowersLoanList.as_view(), name="loans-endpoint"),
    path('loans/requests/', BorrowerLoanRequestList.as_view(), name="loans-requests-lists-endpoint"),
    path('loans/<int:pk>/', LoansDetail.as_view(), name="loans-detail-endpoint"),
    path('loans/history/', TransactionHistory.as_view(), name="loans-history-endpoint")
]