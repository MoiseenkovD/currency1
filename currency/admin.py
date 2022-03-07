from django.contrib import admin
from currency.models import Rate, Source, ContactUs


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sale',
        'created',
        'type',
        'source',
    )

    list_filter = (
        'type',
        'created',
    )

    search_fields = (
        'buy',
        'sale',
        'type',
        'source',
    )

    readonly_fields = (
        'buy',
        'sale',
    )


admin.site.register(Rate, RateAdmin)


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
        'phone',
    )


admin.site.register(Source, SourceAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'name',
        'reply_to',
        'subject',
        'body',
        'raw_content',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)


