import django_filters
from currency.models import Rate


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ['gte', 'lte', 'exact'],
            'sale': ['gte', 'lte', 'exact'],
        }

