from django.contrib import admin
from .models import *

# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ('firstname', 'name','email', 'phone', 'subject', 'city', 'created_at')

class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'city', 'created_at')

class AdminCart(admin.ModelAdmin):
    list_display = ('user',  'product','product_qty', 'created_at')

class AdminWishlist(admin.ModelAdmin):
    list_display = ('user',  'product', 'created_at')

class AdminCategory(admin.ModelAdmin):
    list_display = ('slug', 'name', 'meta_title')

class AdminOrderItem(admin.ModelAdmin):
    list_display = ('id', 'order','product','price', 'created_at')

class AdminOrder(admin.ModelAdmin):
    list_display = ('lname','user', 'phone', 'city', 'total_price', 'payment_mode')

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'selling_price','quantity', 'tag', 'created_at')


admin.site.site_header = "YeniShop"
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Cart, AdminCart)
admin.site.register(Wishlist, AdminWishlist)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderItem, AdminOrderItem)
admin.site.register(Profile, AdminProfile)
admin.site.register(ContactUser, AdminContact)


# EMAIL: yenishop@gmail.com
# username=Yenishop75
# password=Matthias94@


# Compte Tawk to
# Username = Yenishop
# Email = yenishop75@gmail.com
# Password = Matthias75@
# url = yenishop.org


# Il faut installer le gettext
# python manage.py makemessages -l en
# python manage.py makemessages -l fr
# python manage.py compilemessages
