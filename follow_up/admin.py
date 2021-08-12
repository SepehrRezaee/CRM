from django.contrib import admin

from follow_up import models


@admin.register(models.FollowUp)
class AdminFollowUp(admin.ModelAdmin):
    """
    This class add some features to admin
    """
    list_display = [
        'organization',
        'registrar',
        'register_on',
        'content',
    ]

    list_display_links = [
        'organization',
    ]

    list_editable = [
        'content',
    ]

    list_filter = [
        'registrar',
        'register_on',
        'content',
        'organization',
    ]
