import currency
from currency import urls
from currency.api import contacts

from django.contrib import admin
from django.urls import path, include

from currency.views import (
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDeleteView,
    RateDetailsView,
    main,
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceDetailsView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('source/list/', SourceListView.as_view()),
    path('currency/', include(currency.urls))
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
