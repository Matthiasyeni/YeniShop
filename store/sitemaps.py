from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Category

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'contact', 'newsletter']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.created_at

class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.created_at
