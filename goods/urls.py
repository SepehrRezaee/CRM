from django.urls import path

from . import views
from .views import GoodsShow, GoodsUpdate

app_name = 'goods'
urlpatterns = [
    path('products/', GoodsShow.as_view(), name='goods-show'),
    path('update/<int:pk>/', GoodsUpdate.as_view(), name='goods-update'),
    path('download/<str:path>/', views.open_file, name='download-catalog'),
]
