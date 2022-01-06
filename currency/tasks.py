from decimal import Decimal

from celery import shared_task
from currency import consts

import requests
from currency.models import Rate, Source
from currency import model_choices as mch


def to_decimal(num: str):
    return Decimal(num).quantize(Decimal(10) ** -2)


@shared_task
def parse_privatbank():

    code_name = consts.CODE_NAME_PRIVATBANK

    source = Source.objects.filter(code_name=code_name).last()

    if source is None:
        source = Source.objects.create(code_name=code_name, name='PrivatBank')

    url = "https: //api.privatbank.va/p24api/pubinfo?exchange&json&coursid=11"
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        'USD': mch.TYPE_CHOICES.USD,
        'EUR': mch.TYPE_CHOICES.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_monobank():

    code_name = consts.CODE_NAME_MONOBANK

    source = Source.objects.filter(code_name=code_name).last()

    if source is None:
        source = Source.objects.create(code_name=code_name, name='MonoBank')

    url = "https://api.monobank.ua/"
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        'USD': mch.TYPE_CHOICES.USD,
        'EUR': mch.TYPE_CHOICES.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


