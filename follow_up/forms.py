from django import forms
from follow_up.models import FollowUp


class AddFollowUp(forms.ModelForm):
    """
    A form for add some followups
    """

    class Meta:
        model = FollowUp
        fields = [
            'organization',
            'content',
        ]
