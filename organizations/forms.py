from django import forms

from organizations.models import Organizations


class AddOrganization(forms.ModelForm):
    """
    A form for add some organizations
    """

    class Meta:
        model = Organizations
        fields = [
            'brand',
            'landline',
            'state',
            'workers',
            'fullname_audience',
            'products',
            'email',
            'phone_number',
        ]
