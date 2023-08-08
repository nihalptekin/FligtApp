from rest_framework import serializers
from .models import *

class FlightSerializer(serializers.ModelSerializer): 
    class Meta:
        model= Flight
        fields=("__all__")

class ReservationSerializer(serializers.ModelSerializer): 
    class Meta:
        model= Reservation
        fields=("__all__")
    
class PassengerSerializer(serializers.ModelSerializer): 
    class Meta:
        model= Passenger
        fields=("__all__")

