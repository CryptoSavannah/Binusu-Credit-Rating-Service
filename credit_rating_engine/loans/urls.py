from django.urls import path, include
from .views import BorrowersLoanList

urlpatterns = [
    path('loans/', BorrowersLoanList.as_view(), name="loans-endpoint"),
]