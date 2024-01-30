from rest_framework import generics
from .serializers import LogisticCompanySerializer
from ..logistic_auth.models import LogisticCompany
from ...client.client_main.models import Order
from ...client.v1.serializers import OrderSerializer
from ...common.accounts.models import Account
from ...driver.driver_auth.serializers import DriverInfoFullSerializer


class LogisticCompanyListAPIView(generics.ListAPIView):
    queryset = LogisticCompany.objects.all()
    serializer_class = LogisticCompanySerializer


class LogisticCompanyDetailAPIView(generics.ListAPIView):
    queryset = LogisticCompany.objects.all()
    serializer_class = LogisticCompanySerializer
    lookup_field = 'pk'


class OrderListAPIViewForLogistic(generics.ListAPIView):
    queryset = Order.objects.filter(status='New')
    serializer_class = OrderSerializer


class OrderDetailAPIViewForLogistic(generics.RetrieveAPIView):
    queryset = Order.objects.filter(status='New')
    serializer_class = OrderSerializer
    lookup_field = 'pk'


class DriverListAPIView(generics.ListAPIView):
    queryset = Account.objects.filter(role='Driver')
    serializer_class = DriverInfoFullSerializer


class DriverDetailAPIView(generics.RetrieveAPIView):
    queryset = Account.objects.filter(role='Driver')
    serializer_class = DriverInfoFullSerializer
    lookup_field = 'pk'


class MyDriversListAPIView(generics.ListAPIView):
    serializer_class = DriverInfoFullSerializer

    def get_queryset(self):
        queryset = Account.objects.filter(company_company__user=self.request.user)
        return queryset
