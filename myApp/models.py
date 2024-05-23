from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=100, default="N/A")
    lastName = models.CharField(max_length=100, default="N/A")
    username = models.CharField(max_length=12, default="N/A")
    password = models.CharField(max_length=12, default="N/A")
    repassword = models.CharField(max_length=12, default="N/A")
    email = models.EmailField(max_length=255, default="N/A")


    def __str__(self):
        return self.username


