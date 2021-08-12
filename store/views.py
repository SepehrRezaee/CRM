import weasyprint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView

from organizations.models import Organizations
from store.forms import QuoteItemForm, QuoteForm
from store.models import Quote, QuoteItem


class ShowQuote(ListView):
    """
    Shows all of Quotes
    """
    model = Quote
    template_name = 'store/show_quote.html'
    paginate_by = 3


class AddQuote(CreateView):
    """
    Creates a new Quote
    """
    form_class = QuoteForm
    template_name = 'store/add_quote.html'
    success_url = reverse_lazy('store:quote-show')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['pk'] = self.kwargs.get('pk', None)
        return context

    def form_valid(self, form):
        # Sets up the creator and the owner of a quote automatically
        organization_instance = Organizations.objects.get(pk=self.get_context_data().get('pk'))
        form.instance.creator = self.request.user
        form.instance.owner = organization_instance
        form.save()
        return super().form_valid(form)


class DeleteQuote(DeleteView):
    """
    Deletes a Quote
    """
    model = Quote
    template_name = 'store/quote_confirm_delete.html'
    success_url = reverse_lazy('store:quote-show')


class ShowQuoteItem(DetailView):
    """
    Shows detail of a Quote
    """
    model = Quote
    template_name = 'store/show_quote_item.html'

    def quote_items(self):
        # Returns own products of a Quote
        objects_item = self.get_object()
        organization = Quote.objects.get(owner=objects_item.owner, pk=self.kwargs.get('pk', None))
        product = QuoteItem.objects.filter(pre_quote=organization)
        return product

    def get_context_data(self, **kwargs):
        # Returns all items of a quote
        product = self.quote_items()
        contex = super().get_context_data()
        contex['items'] = None
        contex['items'] = product
        return contex


class AddQuoteItem(CreateView):
    """
    Add an item to QuoteItem list
    """
    form_class = QuoteItemForm
    template_name = 'store/add_quote_item.html'
    success_url = reverse_lazy('store:quote-show')

    def get_context_data(self, **kwargs):
        context = super(AddQuoteItem, self).get_context_data()
        context['pk'] = self.kwargs.get('pk', None)
        return context

    def form_valid(self, form):
        # Sets up the pre_quote of a quote item automatically
        pre_quote_instance = Quote.objects.get(pk=self.get_context_data().get('pk'))
        form.instance.pre_quote = pre_quote_instance
        return super().form_valid(form)


class DeleteQuoteItem(DeleteView):
    """
    Deletes a QuoteItem
    """
    model = QuoteItem
    template_name = 'store/quoteitem_confirm_delete.html'
    success_url = reverse_lazy('store:quote-item-show')


class PrintOrder(LoginRequiredMixin, DetailView):
    """
    Print a Quote in a pdf file
    """
    model = Quote
    template_name = 'store/quote_detail.html'

    def get(self, request, *args, **kwargs):
        # Call parents as normal
        g = super(PrintOrder, self).get(request, *args, **kwargs)

        # Get the rendered content and pass it to weasyprint
        rendered_content = g.rendered_content
        pdf = weasyprint.HTML(string=rendered_content, base_url='http://127.0.0.1:8000/').write_pdf()

        # Create a new http response with pdf mime type
        response = HttpResponse(pdf, content_type='application/pdf')
        return response
