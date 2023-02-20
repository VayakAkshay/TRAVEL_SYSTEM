from django.contrib import admin
from .models import MasterPackages,contactform,CustomerData,Review,Booked_package
# Register your models here.

admin.site.register(MasterPackages)
admin.site.register(contactform)
admin.site.register(CustomerData)
admin.site.register(Review)
admin.site.register(Booked_package)

class ImageAdmin(admin.ModelAdmin):
    list_display = ["customer_img","customer_img"]