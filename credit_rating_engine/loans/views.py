from django.shortcuts import render
from .serializers import LoansRetrieveSerializer, LoanPaymentsRetrieveSerializer, LoansFormSerializer, LoansCreateSerializer, UserFormSerializer, UserCreateSerializer
from .models import Loans, LoanPayments
from rest_framework.views import APIView
from rest_framework import status
from .helpers import hash_input, random_string_digits

from rest_framework.response import Response

class RegisterUser(APIView):

    def post(self, request):
        user_data = UserFormSerializer(data=request.data)
        if user_data.is_valid():
            user_number = random_string_digits()

            user_data_request_save = {
                "full_name":user_data.data['full_name'],
                "hashed_nin":hash_input(user_data.data['nin_number']),
                "bnu_address":"some_address",
                "physical_address":user_data.data['physical_address'],
                "user_number": user_number,
                "password":hash_input(user_data.data['password']),
                "refferal_id":user_data.data['refferal_id'],
                "role":user_data.data['role']
            }

            user_date_request_transaction = UserCreateSerializer(data=user_data_request_save)
            user_date_request_transaction.is_valid(raise_exception=True)
            user_date_request_transaction.save()

            data_dict = {"status":201, "user_details":user_date_request_transaction.data}
            return Response(data_dict, status=status.HTTP_201_CREATED)

        return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)


class BorrowersLoanList(APIView):

    def get(self, request, format=None):
        snippets = Loans.objects.all()
        serializer = LoansRetrieveSerializer(snippets, many=True)
        data_dict = {"status":200, "data":serializer.data}
        return Response(data_dict, status=status.HTTP_200_OK)

    def post(self, request):
        loan_request = LoansFormSerializer(data=request.data)
        if loan_request.is_valid():

            loan_request_save = {
                "borrower_address":loan_request.data['borrowers_address'],
                "borrower_nin_hash":loan_request.data['borrower_nin_hash'],
                "loan_amount":loan_request.data['loan_amount'],
                "expected_payment_date": loan_request.data['repayment_date'],
                "loan_status":0,
            }

            loan_request_transaction = LoansCreateSerializer(data=loan_request_save)
            loan_request_transaction.is_valid(raise_exception=True)
            loan_request_transaction.save()

            data_dict = {"status":201, "loan_request_details":loan_request_transaction.data}
            return Response(data_dict, status=status.HTTP_201_CREATED)

        return Response(loan_request.errors, status=status.HTTP_400_BAD_REQUEST)
