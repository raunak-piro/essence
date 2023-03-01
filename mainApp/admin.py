from django.contrib import admin
from .models import *

admin.site.register(
    (
        # Buyer,
        
        # Brand,
        # Product,
        # Checkout,
        # CheckoutProducts,
        # Wishlist,
        # ContectUs,
    )
)

@admin.register(Maincategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id","name")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name","maincategory","subcategory","brand","color","size","baseprice","discount","finalprice","stock","description","pic1")

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ("id","user","orderStatus","paymentMode","paymentStatus","rppid","totalAmount","shippingAmount","finalAmount","time")
@admin.register(CheckoutProducts)
class CheckoutProductsAdmin(admin.ModelAdmin):
    list_display = ("id","checkout","pid","name","color","size","price","qty","total","pic")
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("id","product","user")
@admin.register(ContectUs)
class ContectUsAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","phone","subject","message","status","date")
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id","name","username","email","phone","addressline1","addressline2","addressline3","pin","city","state","pic")