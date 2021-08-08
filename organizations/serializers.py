from rest_framework import serializers

from organizations.models import Organizations


class OrganizationsSerializers(serializers.HyperlinkedModelSerializer):
    """
    Defines the API representation for organizations
    """

    class Meta:
        model = Organizations
        fields = [
            'brand',
            'state',
            'landline',
            'fullname_audience',
            'phone_number',
            'email',
            'date_registration',
            'products',
            'workers',
            'registrar',
        ]
