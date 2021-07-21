from rest_framework import viewsets
from . import models, serializers

class CustomerViewsets(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    