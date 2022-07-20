from django.contrib import admin
from . import models

# Register your models here.
class PMAdminArea(admin.AdminSite):
    site_header = 'Project Management Admin Area'
    index_title = 'Project_Management'
    site_title = 'Project Management'

pm_site = PMAdminArea(name='Project_Management_Admin')

# Admin Area
admin.site.register(models.Supplier)
admin.site.register(models.ItemPricing)
admin.site.register(models.SupplierItem)
admin.site.register(models.Project)
admin.site.register(models.ProjectSCURVE)

# Project Management
pm_site.register(models.Supplier)
pm_site.register(models.ItemPricing)
pm_site.register(models.SupplierItem)
pm_site.register(models.Project)
pm_site.register(models.ProjectSCURVE)