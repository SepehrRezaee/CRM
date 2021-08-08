from rest_framework import serializers

from goods.models import Product, OrganizationProduct


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    """
    Defines the API representation for products
    """

    class Meta:
        model = Product
        fields = [
            'name_product',
            'price',
            'technical_features',
            'includes_taxes',
            'proposed',
        ]


class OrganizationProductSerializers(serializers.HyperlinkedModelSerializer):
    """
    Defines the API representation for organization's products
    """

    class Meta:
        model = OrganizationProduct
        fields = [
            'name',
            'slug',
        ]

        read_only_field = [
            'slug',
        ]
