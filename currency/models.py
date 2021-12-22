from django.db import models
from rest_framework import serializers

from currency import model_choices as mch


class Rate(models.Model):
    class Meta:
        db_table = "rate"

    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(choices=mch.TYPE_CHOICES, default=mch.TYPE_USD)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)


class Source(models.Model):
    class Meta:
        db_table = "source"

    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    logo = models.FileField(upload_to='media/logo', default=None, null=True, blank=True)

    def __str__(self):
        return self.name

# class SourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Source
#         fields = "__all__"


class RequestResponseLog(models.Model):

    path = models.CharField(max_length=255)
    # request_method = models.PositiveSmallIntegerField(choices=mch.RequestResponseLogRequestMethod)
    request_method = models.CharField(max_length=10, choices=mch.RequestResponseLogRequestMethod.choices)
    time = models.FloatField()


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    raw_content = models.TextField()

