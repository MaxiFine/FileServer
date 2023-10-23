from django.urls import path
from accounts.views import signup_view, activation_link, login_view



urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('activate/<uidb64>/<token>/', activation_link, name='activate'),
    path('login/', login_view, name='login'),
    
]

