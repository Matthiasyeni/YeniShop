from django.db import models
import datetime
import os
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import intcomma
from uuid import uuid4

from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('upload/', filename)


# class Category(models.Model):
#     slug = models.CharField(max_length=50, null=False, blank=False)
#     name = models.CharField(max_length=50, null=False, blank=False)
#     image = models.ImageField(upload_to=get_file_path, null=False, blank=True)
#     description = models.TextField(max_length=500, null=False, blank=False)
#     status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
#     trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
#     meta_title = models.CharField(max_length=150, null=False, blank=False)
#     meta_keywords = models.CharField(max_length=150, null=False, blank=False)
#     meta_description = models.CharField(max_length=500, null=False, blank=False)
#     created_at = models.DateTimeField(default=timezone.now)


#     def __str__(self):
#         return self.name


class Category(models.Model):
    slug = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Slug"))
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Name"))
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True, verbose_name=_("Image"))
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name=_("Description"))
    status = models.BooleanField(default=False, help_text=_("0=default, 1=Hidden"), verbose_name=_("Status"))
    trending = models.BooleanField(default=False, help_text=_("0=default, 1=Trending"), verbose_name=_("Trending"))
    meta_title = models.CharField(max_length=150, null=False, blank=False, verbose_name=_("Meta Title"))
    meta_keywords = models.CharField(max_length=150, null=False, blank=False, verbose_name=_("Meta Keywords"))
    meta_description = models.CharField(max_length=500, null=False, blank=False, verbose_name=_("Meta Description"))
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('collectionsview', args=[self.slug])


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    small_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    # quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=50, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_original_price(self):
        original_price_float = float(self.original_price)
        return f"{original_price_float:.0f}"

    def formatted_selling_price(self):
        selling_price_float = float(self.selling_price)
        return f"{selling_price_float:.0f}"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('productview', args=[self.Category.slug, self.slug])


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    # selling_price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(max_length=150, null=False)
    city = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=False)
    orderstatuses = (
        ('Pending', 'Pending'),
        ('Out For Shipping', 'Out For Shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=150, choices= orderstatuses, default='Pending')
    message = models.CharField(max_length=150, null=False)
    tracking_no = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return '{} - {}'.format(self.order.id, self.order.tracking_no)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(max_length=150, null=False)
    city = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user.username

class ContactUser(models.Model):
    firstname = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=50, null=False)
    subject = models.TextField(max_length=550, null=False)
    city = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(default=timezone.now)

 
    def __str__(self):
        return self.name
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# class Invoice(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     # Vos champs de modèle pour les factures
#     pass



# class YourModel(models.Model):
#     # Vos champs de modèle ici

#     def current_year(self):
#         return timezone.now().year