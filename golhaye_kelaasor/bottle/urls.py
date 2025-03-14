from django.urls import path
from bottle.views import sign_up

urlpatterns = [
    path('sign-up', sign_up),
]
