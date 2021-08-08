from django.urls import path

from . import views

app_name = 'follow_up'
urlpatterns = [
    path('register_follow_up/', views.create_follow_up, name='register-follow-up'),
]
