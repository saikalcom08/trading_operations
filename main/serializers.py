from rest_framework import serializers

from .models import (
    Firm,
    Manager,
    Address,
    MeasurementUnit,
    Product,
    PriceHistory,
    Operation,
)


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = "__all__"


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_price(self, obj: Product):
        price_object: PriceHistory = obj.prices.filter(
            date_to__isnull=True
        ).last()
        if price_object is not None:
            return price_object.price


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = "__all__"


class OperationSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    total_sum = serializers.ReadOnlyField()

    class Meta:
        model = Operation
        fields = "__all__"

    def get_total_price(self, obj: Operation):
        actual_price_record: PriceHistory = obj.product.prices.filter(
            date_to__isnull=True
        ).last()
        return obj.quantity * actual_price_record.price
