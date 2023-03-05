from django.contrib import admin
from .models import ProductModel,CartModel,CustomerModel,OrderHistoryModel
# Register your models here.


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','price','img']
    
@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','img']

@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','phoneNo','address']
    
@admin.register(OrderHistoryModel)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','img','dateAndTime']