from django.shortcuts import render
from .serializers import LoansRetrieveSerializer, LoanPaymentsRetrieveSerializer, LoansFormSerializer, LoansCreateSerializer, LoanRequestSerializer, SpendKeySerializer, LoanIdSerializer
from .models import Loans, LoanPayments
from accounts.models import User
from rest_framework.views import APIView
from rest_framework import status
from .helpers import BnuAddressCollector
from accounts.permissions import ClientPermissions
from django.db.models import Avg, Count, Min, Sum
import datetime

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


class GetSpendingKeys(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        address = LoanRequestSerializer(data=request.data)

        if address.is_valid():
            user_account = User.objects.get(bnu_address=address.data['address'])

            serializer = SpendKeySerializer(user_account)
            data_dict = {"status":200, "data":serializer.data}
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)


class LentMoney(APIView):
    
    permission_classes = (permissions.IsAuthenticated, )
    
    def post(self, request):
        address = LoanRequestSerializer(data=request.data)

        if address.is_valid():
            open_loans = Loans.objects.filter(lending_address=address.data['address']).filter(loan_status=2).aggregate(loan_amount = Sum('loan_amount'))

            interest_open_loans = Loans.objects.filter(lending_address=address.data['address']).filter(loan_status=2).aggregate(expected_amount = Sum('expected_amount'))
            
            if open_loans['loan_amount']==None and interest_open_loans['expected_amount']==None:
                data_dict = {"status":200, "data":{"loan_amount":0, "interest":0}}
                return Response(data_dict, status=status.HTTP_200_OK)
            interest = interest_open_loans['expected_amount'] - open_loans['loan_amount']
            data_dict = {"status":200, "data":{"loan_amount":open_loans['loan_amount'], "interest":interest}}
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)


class EditLoanStatus(APIView):
   
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        loanid = LoanIdSerializer(data=request.data)

        if loanid.is_valid():
            loan_to_approve = Loans.objects.get(pk=loanid.data['loan_id'])

            loan_update = {
                "loan_status":loanid.data['status'],
                "date_approved":datetime.date.today(),
                "lending_address":loanid.data['lending_address'],
                "pay_id":loanid.data['pay_id']
            }

            Loans.objects.update_or_create(
                        id=loan_to_approve.pk, defaults=loan_update)

            loan_to_approve_updated = Loans.objects.get(pk=loanid.data['loan_id'])

            serializer = LoansRetrieveSerializer(loan_to_approve_updated)
            data_dict = {"status":200, "data": serializer.data}
            return Response(data_dict, status=status.HTTP_201_CREATED)
        
        return Response(loanid.errors, status=status.HTTP_200_OK)


       

