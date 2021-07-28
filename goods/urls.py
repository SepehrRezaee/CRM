from django.urls import path

from . import views
from .views import ProductsShow, GoodsUpdate

app_name = 'goods'
urlpatterns = [
    path('products/', ProductsShow.as_view(), name='goods-show'),
    path('update/<int:pk>/', GoodsUpdate.as_view(), name='goods-update'),
    path('download/', views.download_file, name='download-catalog'),
]
