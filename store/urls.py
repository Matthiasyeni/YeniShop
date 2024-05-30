from django.contrib import admin
from django.urls import path
from . import views
from django.views.i18n import set_language

from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap

from store.controller import authview, cart, wishlist, checkout
from .sitemaps import StaticViewSitemap, ProductSitemap, CategorySitemap
from .views import contact, generate_invoice, robots_txt


# Dashboard Admin header customization

admin.site.site_header = "YeniShop"
admin.site.site_title = "YeniShop"
admin.site.index_title = "Admin"

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),


    path('product-list', views.productlistAjax),
    path('searchproduct', views.searchproduct, name="searchproduct"),
    
    # path('accounts/', include('allauth.urls')),

    path('contact/', contact, name='contact'),
    path('contact/', views.newsletter, name='newsletter'),

    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),

    # path('generate-invoice/', generate_invoice, name='generate_invoice'),

    path('wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),

    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),
    path('generate-invoice', checkout.generate_invoice, name='generate_invoice'),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),

]


