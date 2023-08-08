
from .models import *
from .serializers import FlightSerializer, ReservationSerializer, PassengerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly

# Create your views here.

class FlightView(viewsets.ModelViewSet): 
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    # permission_classes=[IsAdminUser]
    permission_classes=[IsAdminOrReadOnly]

class ReservationView(viewsets.ModelViewSet): 
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
   

class PassengerView(viewsets.ModelViewSet): 
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer
 