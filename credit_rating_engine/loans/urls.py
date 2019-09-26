from django.urls import path, include
from .views import BorrowersLoanList, RegisterUser

urlpatterns = [
    path('auth/register/', RegisterUser.as_view(), name="register-endpoint"),
    path('loans/', BorrowersLoanList.as_view(), name="loans-endpoint"),
]