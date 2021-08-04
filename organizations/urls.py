from django.urls import path

from . import views
from .views import OrganizationsShow, OrganizationsAdd, OrganizationsUpdate, OrganizationsDetail

app_name = 'organizations'
urlpatterns = [
    path('', OrganizationsShow.as_view(), name='organizations-show'),
    path('add/', OrganizationsAdd.as_view(), name='organizations-add'),
    path('update/<int:pk>/', OrganizationsUpdate.as_view(), name='organizations-update'),
    path('detail/<int:pk>/', OrganizationsDetail.as_view(), name='organizations-detail'),
    path('send_email/<int:pk>/', views.send_email, name='send-email'),
    # path('send_email/', views.send_email, name='send-email'),
]