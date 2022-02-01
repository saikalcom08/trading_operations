from .models import *
from .serializers import *
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from django.db.models import QuerySet, F, Q


# Create your views here.
class FirmViewSet(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=["GET"], detail=False, url_path="by-price")
    def get_products_by_price(self, request: Request, *args, **kwargs):
        queryset = self.get_queryset()

        value = request.query_params.get("value")

        if value is not None:
            queryset = queryset.filter(
                prices__date_to__isnull=True, prices__price__lte=value
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "Value is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class MeasurementUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer


class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer


class ListOfProductsByPriceView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        value = self.request.query_params.get("value")

        queryset = super().get_queryset()
        if value is not None:
            queryset = queryset.filter(
                prices__date_to__isnull=True, prices__price__lt=value
            )
        return queryset


class OperationsWithCalculationsView(generics.ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

    def get_queryset(self):
        queryset: QuerySet = super().get_queryset()
        return queryset.annotate(
            actual_price=F("product__prices__price")
        ).annotate(total_sum=F("actual_price") * F("quantity"))
