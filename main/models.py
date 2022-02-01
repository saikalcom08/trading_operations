from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Firm(models.Model):
    name = models.CharField(_("Название"), max_length=100)

    class Meta:
        verbose_name = _("Фирма")
        verbose_name_plural = _("Фирмы")


class Address(models.Model):
    firm = models.OneToOneField(
        Firm,
        verbose_name=_("Firm"),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    street = models.CharField(_("Street"), max_length=50)
    building = models.CharField(_("Building"), max_length=50)
    appartment = models.CharField(_("Appartment"), max_length=50)
    city = models.CharField(_("City"), max_length=50)
    country = models.CharField(_("Country"), max_length=50)


class Manager(models.Model):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    father_name = models.CharField(_("Father Name"), max_length=100)
    date_from = models.DateField(
        _("Date From"), auto_now=False, auto_now_add=False
    )
    date_to = models.DateField(
        _("Date to"), auto_now=False, auto_now_add=False, null=True
    )
    firm = models.ForeignKey(
        Firm, verbose_name=_("Firm"), on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = _("Manager")
        verbose_name_plural = _("Managers")


class MeasurementUnit(models.Model):
    title = models.CharField(_("Title"), max_length=100)

    class Meta:
        verbose_name = _("MeasurementUnit")
        verbose_name_plural = _("MeasurementUnits")

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    unit = models.ForeignKey(
        MeasurementUnit, verbose_name=_("Unit"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title


class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        related_name="prices",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    date_from = models.DateField(
        _("Date from"), auto_now=False, auto_now_add=False
    )
    date_to = models.DateField(
        _("Date to"), auto_now=False, auto_now_add=False, null=True
    )

    def __str__(self):
        return str(self.price)


class Operation(models.Model):
    firm = models.ForeignKey(
        Firm, verbose_name=_("Firm"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, verbose_name=_("Product"), on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(_("Quantity"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Operation")
        verbose_name_plural = _("Operations")
