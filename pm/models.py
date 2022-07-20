from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ItemPricing(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=20)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item's Pricing"


class SupplierItem(models.Model):
    supplier_id = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    item_id = models.ForeignKey(
        ItemPricing,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Suppliers' Item Pricing"


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=False, null=True, blank=True)
    end_date = models.DateField(auto_now_add=False, null=True, blank=True)
    budget = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class ProjectSCURVE(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    item = models.CharField(max_length=10)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField()
    percentage = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'S-CURVE'


# class BillOfQuantities(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True, blank=True)
#     item = models.IntegerField()
#     description = models.CharField(max_length=255, null=True, blank=True)
#     quantity = models.IntegerField()
#     unit = models.CharField(max_length=10, null=True, blank=True)
#     unit_cost = models.IntegerField()
#     material_cost = models.IntegerField()
#