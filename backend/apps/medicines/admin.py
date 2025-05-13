from django.contrib import admin
from .models import Medicine
# Register your models here.
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name','brand','price','stock', 'mg', 'expiry_date',]

admin.site.register(Medicine, MedicineAdmin)

# Credentials for the admin panel:
# username: MedCoHub
# password: Medicine123#
# The above credentials are for the admin panel of the medicines app.
