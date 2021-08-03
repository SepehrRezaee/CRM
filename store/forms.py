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
            'pre_quote',
            'qty',
            'discount',
        ]


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            'owner',
        ]