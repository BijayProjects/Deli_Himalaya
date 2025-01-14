from django.contrib import admin
from .models import Category,Product,Customer,CustomerOrder,Feedback
# Register your models here.
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','image','product_name','price','description','delivery_charge','category']

@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display=['id','customerName','phoneNumber','email','city','region','street_address','zip_code','product_name','product_price','total']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display =['id','fullname','email','message']