from currency.api import contacts

from django.contrib import admin
from django.urls import path

from currency.views import (
    rate_list, rate_create, rate_update, rate_delete, rate_details, main, index,
    get_by_id, create, update, delete
)
from currency.api import source_create, source_update, source_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:pk>/', rate_update),
    path('rate/delete/<int:pk>/', rate_delete),
    path('rate/details/<int:pk>/', rate_details),
    path('contacts/us', contacts.ContactsApi.as_view()),
    path('', main),
    path('index/', index),
    path('source/<int:id>', get_by_id),
    path('index/source/create', create),
    path('index/source/update', update),
    path('index/source/delete', delete),
    path('api/source/create', source_create.SourceCreate.as_view()),
    path('api/source/update', source_update.SourceUpdate.as_view()),
    path('api/source/delete', source_delete.SourceDelete.as_view()),
]