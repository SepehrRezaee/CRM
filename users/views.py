from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer


class Logout(LogoutView):
    """
    This view uses for logout from account
    """
    template_name = 'organizations/show_organization.html'
    success_url = reverse_lazy('organizations:organizations-show')


"""
DRF Views
"""


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
