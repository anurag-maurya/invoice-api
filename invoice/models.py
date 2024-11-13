from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self) -> str:
        return self.invoice_number
    
class InvoiceDetail(models.Model):
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE, related_name="details")
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    line_total = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self) -> str:
        return f"Detail for {self.invoice.invoice_number}"

    
    
    
