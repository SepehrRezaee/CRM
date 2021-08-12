from django.urls import path

from store import views
from store.views import AddQuoteItem, ShowQuote, AddQuote, ShowQuoteItem, DeleteQuote, DeleteQuoteItem

app_name = 'store'
urlpatterns = [
    path('quote_show/', ShowQuote.as_view(), name='quote-show'),
    path('quote-item-show/<int:pk>/', ShowQuoteItem.as_view(), name='quote-item-show'),
    path('add_quote/<int:pk>/', AddQuote.as_view(), name='add-quote'),
    path('add_quote_item/<int:pk>/', AddQuoteItem.as_view(), name='add-quote-item'),
    path('delete/<int:pk>/', DeleteQuote.as_view(), name='delete-quote'),
    path('delete_item/<int:pk>/', DeleteQuoteItem.as_view(), name='delete-quote-item'),
    path('print/<int:pk>/', views.PrintOrder.as_view(), name='print-order'),
]
