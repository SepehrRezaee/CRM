from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from rest_framework import mixins, viewsets, permissions

from goods.models import Product
from organizations.forms import AddOrganization
from organizations.models import Organizations
from organizations.serializers import OrganizationsSerializers
from organizations.tasks import task
from store.models import Quote


class OrganizationsShow(ListView):
    """
    Show all organizations and their information
    """
    model = Organizations
    template_name = 'organizations/show_organization.html'
    paginate_by = 3


class OrganizationsAdd(CreateView):
    """
    Add some new organizations
    """
    model = Organizations
    form_class = AddOrganization
    template_name = 'organizations/add_organizaton.html'
    success_url = reverse_lazy('organizations:organizations-show')

    def form_valid(self, form):
        form.instance.registrar = self.request.user
        registrar = form.instance.registrar
        registrar.save()
        return super().form_valid(form)


class OrganizationsUpdate(UpdateView):
    """
    Updates information of an organization
    """
    model = Organizations
    template_name = "organizations/update_organization.html"
    success_url = reverse_lazy('organizations:organizations-show')

    fields = [
        'brand',
        'landline',
        'state',
        'workers',
        'fullname_audience',
        'products',
        'email',
    ]


class OrganizationsDetail(DetailView):
    model = Organizations
    template_name = 'organizations/info_organization.html'

    def related_products(self):
        """
        Shows all of proposed products for organization products
        """
        organization = self.get_object()
        related_products = organization.products.all()
        suggestions_product = Product.objects.filter(proposed__in=related_products).distinct()
        return suggestions_product

    def get_context_data(self, **kwargs):
        products = self.related_products()
        contex = super().get_context_data()
        contex['suggestion_product'] = products
        return contex


def send_email(request, pk):
    quote = get_object_or_404(klass=Quote, pk=pk)
    sender = request.user.get_full_name()
    content = render_to_string(context={'object': quote}, template_name='store/quote_detail.html')
    receiver = quote.owner.brand
    task(content, receiver, sender)
    return redirect(reverse_lazy('store:quote-show'))


"""
DRF Views
"""


class OwnOrganizations(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """
    An API for shows information of organizations
    """
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializers
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'registrar'

    def get_queryset(self):
        qs = Organizations.objects.filter(registrar=self.request.user)
        return qs
