from django.urls import path
from bottle.views import sign_up, new_message

urlpatterns = [
    path('sign-up', sign_up),
    path('new-message', new_message)
]
