from django.http import JsonResponse
from django.views.generic import ListView, CreateView
from rest_framework import status

from follow_up.models import FollowUp
from organizations.models import Organizations


class CreateFollowUp(CreateView):
    """
    Creates a follow up for an organization
    """
    model = FollowUp
    template_name = 'add_follow_up.html'
    fields = [
        'content',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['pk'] = self.kwargs.get('pk', None)
        return context

    def form_valid(self, form):
        organization_instance = Organizations.objects.get(pk=self.get_context_data().get('pk'))
        form.instance.organization = organization_instance
        form.instance.registrar = self.request.user
        form.save()
        return JsonResponse(
            data={
                'success': True
            }
            , status=status.HTTP_200_OK
        )


class ShowFollowUp(ListView):
    """
    Displays all of each registration follow ups of an organization
    """
    model = FollowUp
    template_name = 'show_follow_up.html'
    queryset = FollowUp.objects.all()

    def get_queryset(self):
        qs = self.queryset
        return qs.filter(organization__pk=self.kwargs.get('pk'))
