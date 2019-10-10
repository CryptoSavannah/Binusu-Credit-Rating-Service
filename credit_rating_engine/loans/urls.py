from django.urls import path, include
from .views import BorrowersLoanList, BorrowerLoanRequestList, LoansDetail, TransactionHistory, GetSpendingKeys, LentMoney, EditLoanStatus

urlpatterns = [
    path('loans/', BorrowersLoanList.as_view(), name="loans-endpoint"),
    path('loans/requests/', BorrowerLoanRequestList.as_view(), name="loans-requests-lists-endpoint"),
    path('loans/<int:pk>/', LoansDetail.as_view(), name="loans-detail-endpoint"),
    path('loans/history/', TransactionHistory.as_view(), name="loans-history-endpoint"),
    path('loans/get_key/', GetSpendingKeys.as_view(), name="loans-getkeys-endpoint"),
    path('loans/stats/', LentMoney.as_view(), name="loans-statistics"),
    path('loans/update/', EditLoanStatus.as_view(), name="update-loan")
]