from django.shortcuts import render
from .serializers import LoansRetrieveSerializer, LoanPaymentsRetrieveSerializer, LoansFormSerializer, LoansCreateSerializer, LoanRequestSerializer
from .models import Loans, LoanPayments
from rest_framework.views import APIView
from rest_framework import status
from .helpers import BnuAddressCollector
from accounts.permissions import ClientPermissions

from rest_framework.response import Response
from rest_framework import permissions


class BorrowersLoanList(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, format=None):
        snippets = Loans.objects.filter(loan_status=0)
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
                "expected_amount": loan_request.data['expected_amount']
            }

            loan_request_transaction = LoansCreateSerializer(data=loan_request_save)
            loan_request_transaction.is_valid(raise_exception=True)
            loan_request_transaction.save()

            data_dict = {"status":201, "loan_request_details":loan_request_transaction.data}
            return Response(data_dict, status=status.HTTP_201_CREATED)

        return Response(loan_request.errors, status=status.HTTP_400_BAD_REQUEST)


class BorrowerLoanRequestList(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        borrower_requests = LoanRequestSerializer(data=request.data)
        loan_status = self.request.query_params.get('status', None)

        if borrower_requests.is_valid():
            if loan_status=="unapproved":
                loan_requests=Loans.objects.filter(borrower_address=borrower_requests.data['address']).filter(loan_status=0)
            elif loan_status=="unpaid":
                loan_requests=Loans.objects.filter(borrower_address=borrower_requests.data['address']).filter(loan_status=2)


            serializer = LoansRetrieveSerializer(loan_requests, many=True)
            data_dict = {"status":200, "data":serializer.data}
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response(loan_request.errors, status=status.HTTP_400_BAD_REQUEST)

class LoansDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, pk, format=None):
        particular_loan = Loans.objects.get(pk=pk)
        serializer = LoansRetrieveSerializer(particular_loan)
        data_dict = {"data":serializer.data, "status":200}
        return Response(data_dict, status=status.HTTP_200_OK)


class TransactionHistory(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        address = LoanRequestSerializer(data=request.data)
        role = self.request.query_params.get('role', None)

        if address.is_valid():
            if role=="borrower":
                loan_requests=Loans.objects.filter(borrower_address=address.data['address']).filter(loan_status=4)
            elif role=="lender":
                loan_requests=Loans.objects.filter(lending_address=address.data['address']).filter(loan_status=4)


            serializer = LoansRetrieveSerializer(loan_requests, many=True)
            data_dict = {"status":200, "data":serializer.data}
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)
       

