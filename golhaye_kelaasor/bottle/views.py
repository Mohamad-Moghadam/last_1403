from django.shortcuts import render
from django.http.response import HttpResponse
from bottle.models import User, Message
import json


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        data = json.loads(request.body)
        User.objects.create(
            first_name = data.get("first_name"),
            last_name = data.get("last_name"),
            phone_number = data.get("phone_number")
            )
        return HttpResponse("دمدم گرم")


def new_message(request):
    if request == "POST":
        data = json.load(request.body)
        Message.objects.create(
            sender = data.get("sender"),
            reciver = data.get("reciver"),
            text = data.get("text"),
        )