from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("firms", views.FirmViewSet)
router.register("managers", views.ManagerViewSet)
router.register("addresses", views.AddressViewSet)
router.register("products", views.ProductViewSet)
router.register("operations", views.OperationViewSet)
router.register("price-history", views.PriceHistoryViewSet)
router.register("units", views.MeasurementUnitViewSet)


urlpatterns = [
    # path("products-by-price/", views.ListOfProductsByPriceView.as_view())
    path("calculations/", views.OperationsWithCalculationsView.as_view())
]

urlpatterns += router.urls
