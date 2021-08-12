from django.contrib import admin
from . import models


@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    """
    This class add some features to admin
    """
    list_display = [
        'name_product',
        'price',
        'technical_features',
        'includes_taxes',
    ]

    list_editable = [
        'price',
        'includes_taxes',
    ]

    list_filter = [
        'price',
        'includes_taxes',
    ]


@admin.register(models.OrganizationProduct)
class OrganizationProduct(admin.ModelAdmin):
    """
    This class add some features to admin
    """
    list_display = [
        'name',
        'slug',
    ]
    list_editable = [
        'slug',
    ]
