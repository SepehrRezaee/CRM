from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy

from users.views import Logout

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     success_url=reverse_lazy('organizations:organizations-show')), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
