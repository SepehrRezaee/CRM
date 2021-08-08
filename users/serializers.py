from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Defines the API representation for users
    """

    class Meta:
        model = get_user_model()
        fields = [
            'pk',
            'username',
            'email',
        ]
        read_only_fields = [
            'pk',
        ]
