from django.db import models
from rest_framework import serializers

from currency import model_choices as mch


class Rate(models.Model):
    class Meta:
        db_table = "rate"

    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(max_length=3, choices=mch.TYPE_CHOICES, default=mch.TYPE_USD)
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    class Meta:
        db_table = "contacts_us"

    email_from = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class Source(models.Model):
    class Meta:
        db_table = "source"

    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"

