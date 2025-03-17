# views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TransportOrder, Waypoint
from .serializers import TransportOrderSerializer, WaypointSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TransportOrderViewSet(viewsets.ModelViewSet):
    queryset = TransportOrder.objects.all()
    serializer_class = TransportOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_date', 'customer_name']
    
class WaypointViewSet(viewsets.ModelViewSet):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer
