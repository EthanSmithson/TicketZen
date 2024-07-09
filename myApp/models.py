from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=100, default="")
    lastName = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=12, default="")
    password = models.CharField(max_length=12, default="")
    repassword = models.CharField(max_length=12, default="")
    email = models.EmailField(max_length=255, default="")
    confirmed = models.IntegerField(default=0)
    activateUUID = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.username
    

class savedTicket(models.Model):
    uid = models.CharField(max_length=10, default="")
    ticket = models.CharField(max_length=1000000000, default="")

    def __str__(self):
        return self.uid

