from rest_framework import viewsets

from celery import shared_task
from api.v1.filters import RateFilter
from api.v1.pagination import RatePagination
from api.v1.serializer import RateSerializer, SourceSerializer, ContactUsSerializer
from api.v1.throttles import AnonCurrencyThrottle
from currency.models import Rate, Source, ContactUs


from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from test import contact_us

from django.core.mail import send_mail
from django.conf import settings


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'sale', 'buy']
    throttle_classes = [AnonCurrencyThrottle]


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    ordering_fields = ['id', 'email_to']
    filterset_fields = ['email_to', ]

    def perform_create(self, serializer):
        super().perform_create(serializer)
        subject = serializer.data['subject']
        body = serializer.data['body']
        email_to = serializer.data['email_to']

        email_body = f'''
                Email From: {email_to}
                Body: {body}
                '''
        contact_us.apply_async(args=(subject, email_body))