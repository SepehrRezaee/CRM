from django.urls import path

from .views import OrganizationsShow, OrganizationsAdd, OrganizationsUpdate, OrganizationsDetail

app_name = 'organizations'
urlpatterns = [
    path('', OrganizationsShow.as_view(), name='organizations-show'),
    path('add/', OrganizationsAdd.as_view(), name='organizations-add'),
    path('update/<int:pk>/', OrganizationsUpdate.as_view(), name='organizations-update'),
    path('detail/<int:pk>/', OrganizationsDetail.as_view(), name='organizations-detail'),
]