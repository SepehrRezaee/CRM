from django import forms

from store.models import QuoteItem, Quote


class QuoteItemForm(forms.ModelForm):
    """
    Add some fields for create a quote for an organization
    """

    class Meta:
        model = QuoteItem
        fields = [
            'product',
            'qty',
            'discount',
        ]


class QuoteForm(forms.ModelForm):
    """
    Add some fields for create a quote item for an quote
    """

    class Meta:
        model = Quote
        fields = [
            'slug',
        ]
