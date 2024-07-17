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
    zeroFlightTotalDuration = models.CharField(max_length=1000000000, default="")
    zeroFirstFlightDepartureDate = models.CharField(max_length=1000000000, default="")
    zeroFirstFlightDepartureAirport = models.CharField(max_length=1000000000, default="")
    zeroFirstFlightArrivalAirport = models.CharField(max_length=1000000000, default="")
    zeroFirstFlightArrivalDate = models.CharField(max_length=1000000000, default="")
    oneFirstFlightDepartureAirport = models.CharField(max_length=1000000000, default="")
    oneFlightTotalDuration = models.CharField(max_length=1000000000, default="")
    oneFirstFlightDepartureDate = models.CharField(max_length=1000000000, default="")
    oneFirstFlightArrivalAirport = models.CharField(max_length=1000000000, default="")
    oneFirstFlightArrivalDate = models.CharField(max_length=1000000000, default="")
    origin = models.CharField(max_length=1000000000, default="")
    destination = models.CharField(max_length=1000000000, default="")
    departureDate = models.CharField(max_length=1000000000, default="")
    returnDate = models.CharField(max_length=1000000000, default="")
    price = models.CharField(max_length=1000000000, default="")

    def __str__(self):
        return self.uid

