from django.shortcuts import render
from django.http.response import HttpResponse
from bottle.models import User, Message
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = json.loads(request.body)
        User.objects.create(
            first_name = data.get("first_name"),
            last_name = data.get("last_name"),
            phone_number = data.get("phone_number")
            )
        return HttpResponse("دمدم گرم")

@csrf_exempt
def new_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Message.objects.create(
            sender_id = data.get("sender"),
            text = data.get("text"),
        )
        return HttpResponse(f"{data.get("text")}")