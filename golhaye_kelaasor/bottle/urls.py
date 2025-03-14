from django.urls import path
from bottle.views import sign_up, new_message , list_messages

urlpatterns = [
    path('sign-up', sign_up),
    path('new-message', new_message),
    path('list-message', list_messages)
]
