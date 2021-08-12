from django.contrib import admin
from . import models


@admin.register(models.Organizations)
class AdminOrganizations(admin.ModelAdmin):
    """
    This class add some features to admin
    """
    list_display = [
        'brand',
        'landline',
        'state',
        'workers',
        'fullname_audience',
        'date_registration',
        'registrar',
        'email',
        'phone_number',
    ]

    list_display_links = [
        'landline',
    ]

    list_editable = [
        'workers',
        'fullname_audience',
        'email',
        'phone_number',
    ]

    list_filter = [
        'state',
        'workers',
    ]


@admin.register(models.EmailHistory)
class AdminEmailHistory(admin.ModelAdmin):
    """
    This class add some features to admin
    """
    list_display = [
        'sender',
        'receiver',
        'sends_on',
        'status',
    ]

    list_display_links = [
        'receiver',
    ]

    list_filter = [
        'sender',
        'receiver',
        'sends_on',
        'status',
    ]
