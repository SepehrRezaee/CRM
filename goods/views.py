import mimetypes
import os

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from rest_framework import mixins, viewsets, permissions

from goods.models import Product, OrganizationProduct
from goods.serializers import ProductSerializers, OrganizationProductSerializers


class ProductsShow(ListView):
    """
    Shows all products of employer
    """
    model = Product
    template_name = 'goods/show_products.html'
    paginate_by = 3


class GoodsUpdate(UpdateView):
    """
    Updates information of products
    """
    model = Product
    template_name = 'goods/update_products.html'
    success_url = reverse_lazy('goods:goods-show')

    fields = [
        'name_product',
        'price',
        'includes_taxes',
    ]


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Easy_MIG_501_T32efc260.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/catalogs/pdf/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


"""
DRF Views
"""


class OwnProduct(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    """
    An API for shows information of product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'proposed'


class OwnOrganizationProduct(viewsets.ModelViewSet):
    """
    An API for shows information of organization's product
    """
    queryset = OrganizationProduct.objects.all()
    serializer_class = OrganizationProductSerializers
    permission_classes = [permissions.IsAuthenticated]
