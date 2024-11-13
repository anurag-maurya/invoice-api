from django.urls import path, include
from invoice.api.views import InvoiceViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',InvoiceViewset)

urlpatterns = [
    path('', include(router.urls)),
]