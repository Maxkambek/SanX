from rest_framework import generics
from .serializers import LogisticCompanySerializer
from ..logistic_auth.models import LogisticCompany
from ...client.client_main.models import Order
from ...client.v1.serializers import OrderSerializer
from ...common.accounts.models import Account
from ...driver.driver_auth.serializers import DriverInfoFullSerializer
from ...tools.pagination import LargeResultsSetPagination


class LogisticCompanyListAPIView(generics.ListAPIView):
    serializer_class = LogisticCompanySerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        queryset = LogisticCompany.objects.all()
        search = self.request.query_params.get('search')
        country = self.request.query_params.get('country_id')
        if search:
            queryset = queryset.filter(company_name__icontains=search)
        if country:
            queryset = queryset.filter(country_id=country)
        return queryset


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
