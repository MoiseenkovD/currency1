import currency
from currency import urls
from currency.api import contacts

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

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
    path('auth/', include('django.contrib.auth.urls')),
    path('', main, name='main'),
    path('source/list/', SourceListView.as_view()),
    path('currency/', include('currency.urls')),
    path('account/', include('account.urls'))
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
