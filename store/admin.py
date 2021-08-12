from django.contrib import admin
from . import models


@admin.register(models.Quote)
class AdminOrganizations(admin.ModelAdmin):
    """
    This class add some features to admin
    """
    list_display = [
        'creator',
        'slug',
        'owner',
        'created',
    ]

    list_display_links = [
        'slug',
    ]

    list_filter = [
        'owner',
        'created',
        'owner',
    ]


@admin.register(models.QuoteItem)
class AdminOrganizations(admin.ModelAdmin):
    """
    This class add some features to admin
    """
    list_display = [
        'product',
        'pre_quote',
        'qty',
        'discount',
    ]

    list_display_links = [
        'pre_quote',
    ]

    list_editable = [
        'qty',
        'discount',
    ]

    list_filter = [
        'pre_quote',
    ]
