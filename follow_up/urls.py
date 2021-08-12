from django.urls import path

from . import views
from .views import ShowFollowUp, CreateFollowUp

app_name = 'follow_up'
urlpatterns = [
    # path('create_follow_up/<int:pk>/', views.register_follow_up, name='register-follow-up'),
    # path('show_template_follow_up/<int:pk>/', views.show_template_follow_up, name='show-template-follow-up'),
    path('create_follow_up/<int:pk>/', CreateFollowUp.as_view(), name='create-follow-up'),
    path('show_follow_up/<int:pk>/', ShowFollowUp.as_view(), name='show-follow-up'),
]
