from django.urls import path
from .views import *
urlpatterns = [
    #path('registration/', UserCreateView.as_view(), name='registration'),
    path('register/', SignUp.as_view(), name='registration'),
]
