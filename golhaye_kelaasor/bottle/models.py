from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)


class Message(models.Model):
    sender = models.ForeignKey(to=User , on_delete=models.PROTECT , related_name="sender_user" )
    reciver = models.ForeignKey(to=User , on_delete=models.PROTECT , related_name="reciver_user")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)