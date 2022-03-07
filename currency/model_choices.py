from django.db import models

TYPE_USD = 1
TYPE_EUR = 2

TYPE_CHOICES = (
    (TYPE_USD, 'Dollar'),
    (TYPE_EUR, 'Euro'),
)


# class RequestResponseLogRequestMethod(models.IntegerChoices):
#     GET = 1, 'GET'
#     POST = 2, 'POST'

class RequestResponseLogRequestMethod(models.TextChoices):
    GET = 'GET', 'GET'
    POST = 'POST', 'POST'
