from django.urls import path
from bottles.views import sign_up

urlpatterns = [
    path('sign-up', sign_up),
]
