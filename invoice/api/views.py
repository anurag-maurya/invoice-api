
from invoice.models import Invoice
from .serializers import InvoiceSerializer
from rest_framework import viewsets
# Create your views here.


class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get','post','put']
        


