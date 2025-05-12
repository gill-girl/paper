from django.contrib import admin

# Register your models here.
from .models import flower, contactform, Order, BookingForm
from. models import  customer,category
# Register your models here.

class flowerAdmin(admin.ModelAdmin):
    list_display=['id','flowername','price']

class customerAdmin(admin.ModelAdmin):
    list_display=['firstname','address']

class bookingAdmin(admin.ModelAdmin):
    list_display=['bookingnumber','firstname','lastname']

class orderAdmin(admin.ModelAdmin):
    list_display=['orderid','ocassion']

class contactAdmin(admin.ModelAdmin):

    list_display=['firstname','phone']

admin.site.register(category)
admin.site.register(flower,flowerAdmin)
admin.site.register(customer,customerAdmin)
admin.site.register(BookingForm,bookingAdmin)
admin.site.register(Order,orderAdmin)
admin.site.register(contactform,contactAdmin)
