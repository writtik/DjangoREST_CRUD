from customer.viewsets import CustomerViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', CustomerViewsets)