from invoice.models import Invoice, InvoiceDetail
from rest_framework import serializers


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        exclude = ("invoice",)

    def validate(self, data):
        if data.get("quantity") <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        if data.get("price") <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return data


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailsSerializer(many=True)
    
    class Meta:
        model = Invoice
        fields = "__all__"
    


    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)

        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)

        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')

        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        existing_details = {detail.id: detail for detail in instance.details.all()}

        for detail_data in details_data:
            detail_id = detail_data.get('id', None)
            if detail_id and detail_id in existing_details:
                detail = existing_details.pop(detail_id)
                detail.description = detail_data.get('description', detail.description)
                detail.quantity = detail_data.get('quantity', detail.quantity)
                detail.price = detail_data.get('price', detail.price)
                detail.line_total = detail_data.get('line_total', detail.quantity * detail.price)
                detail.save()
            else:
                # detail_data['line_total'] = detail_data.get('line_total', detail_data['quantity'] * detail_data['price'])
                InvoiceDetail.objects.create(invoice=instance, **detail_data)

        for detail in existing_details.values():
            detail.delete()

        return instance
        