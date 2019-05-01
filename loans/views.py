from rest_framework import generics

from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404

from .models import Loans
from .serializers import LoansSerializer

def index(request):
    return HttpResponse("Hello, word.")


class LoansList(generics.ListCreateAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer


class LoanDetail(generics.RetrieveDestroyAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer