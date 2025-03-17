from django.db import models

class TransportOrder(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=200)
    order_date = models.DateTimeField()

    def __str__(self):
        return self.order_number

class Waypoint(models.Model):
    ORDER_TYPE_CHOICES = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    ]
    location_name = models.CharField(max_length=200)
    waypoint_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES)
    transport_order = models.ForeignKey(TransportOrder, related_name='waypoints', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['transport_order']

    def __str__(self):
        return f"{self.waypoint_type} - {self.location_name}"
