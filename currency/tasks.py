from decimal import Decimal

from celery import shared_task
from currency import consts

from bs4 import BeautifulSoup as bs

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


@shared_task
def parse_ukrsibbank():
    r = requests.get('https://my.ukrsibbank.com/ru/personal/operations/currency_exchange/')
    html = bs(r.content, 'html.parser')

    USD_TR_INDEX = 0
    EUR_TR_INDEX = 1

    currenciesRatesTRs = html.select('.currency__table > tbody tr')

    usd_buy = currenciesRatesTRs[USD_TR_INDEX].select('td')[1].contents[1]
    usd_sale = currenciesRatesTRs[USD_TR_INDEX].select('td')[2].contents[1]

    eur_buy = currenciesRatesTRs[EUR_TR_INDEX].select('td')[1].contents[1]
    eur_sale = currenciesRatesTRs[EUR_TR_INDEX].select('td')[2].contents[1]

    print('USD:', usd_buy, usd_sale)
    print('EUR:', eur_buy, eur_sale)


@shared_task
def parse_minfin():
    r = requests.get('https://minfin.com.ua/currency/')
    html = bs(r.content, 'html.parser')

    currenciesRatesDivs = html.select('.mfm-grey-bg > table > tbody > tr')

    currencyUSD = currenciesRatesDivs[0].select('td')[1]
    currencyEUR = currenciesRatesDivs[1].select('td')[1]

    usd_buy = currencyUSD.contents[0].strip()
    usd_sale = currencyUSD.contents[2].strip()

    eur_buy = currencyEUR.contents[0].strip()
    eur_sale = currencyEUR.contents[2].strip()

    print(f'''USD - buy: {usd_buy}, sale: {usd_sale}''')

    print(f'''EUR - buy: {eur_buy}, sale: {eur_sale}''')


@shared_task
def parse_kurs():
    r = requests.get('https://kurs.com.ua/')
    html = bs(r.content, 'html.parser')

    currenciesRates = html.select('#main_table > tbody > tr')

    currencyUSD_BUY = currenciesRates[0].select('td')[1]
    currencyEUR_BUY = currenciesRates[1].select('td')[1]

    currencyUSD_SAlE = currenciesRates[0].select('td')[2]
    currencyEUR_SAlE = currenciesRates[1].select('td')[2]

    print(f'''USD - buy: {currencyUSD_BUY.text}USD - sale: {currencyUSD_SAlE.text}''')

    print(f'''EUR - buy: {currencyEUR_BUY.text}EUR - sale: {currencyEUR_SAlE.text}''')



@shared_task
def parse_vkurse():

    url = 'http://vkurse.dp.ua/'

    r = requests.get(url)
    html = bs(r.content, 'html.parser')

    for i in html.select('.container .col-xs-4.section-course'):
        test = i.select('.pokupka-section > .pokupka-value')
        print(test[0])
