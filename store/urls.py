from django.urls import path

from store import views
from store.views import QuoteItemAdd, QuoteShow, QuoteAdd, QuoteItemShow, QuoteDelete, QuoteItemDelete

app_name = 'store'
urlpatterns = [
    path('quote_show/', QuoteShow.as_view(), name='quote-show'),
    path('quote-item-show/<int:pk>/', QuoteItemShow.as_view(), name='quote-item-show'),
    path('add_quote/', QuoteAdd.as_view(), name='add-quote'),
    path('add_quote_item/', QuoteItemAdd.as_view(), name='add-quote-item'),
    path('delete/<int:pk>/', QuoteDelete.as_view(), name='delete-quote'),
    path('delete_item/<int:pk>/', QuoteItemDelete.as_view(), name='delete-quote-item'),
    path('print/<int:pk>/', views.PrintOrder.as_view(), name='print-order'),
]
