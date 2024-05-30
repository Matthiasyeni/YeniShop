from django.shortcuts import redirect, render 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Cart, Order, OrderItem,Product,Profile
from django.contrib.auth.models import User
import random

@login_required(login_url='loginpage')
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product_qty:
            Cart.objects.delete(id=item.id)

        cartitems = Cart.objects.filter(user=request.user)
        total_price = 0
        for item in cartitems:
            total_price = total_price + item.product.selling_price * item.product_qty
    
    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cartitems': cartitems, 'total_price':total_price, 'userprofile':userprofile}
    return render(request, 'store/checkout.html', context)

@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.country = request.POST.get('country')
            userprofile.save()

        neworder = Order() 
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.country = request.POST.get('country')

        neworder.payment_mode = request.POST.get('payment_mode')
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno = 'yeni'+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
           trackno = 'yeni'+str(random.randint(1111111,9999999)) 

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            ) 
# To decrease the product quantity from avalaible stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

# To clear user's Cart
            Cart.objects.filter(user=request.user).delete()

            messages.success(request, "Your order has been placed successfully")
    return redirect('/')



@login_required
def generate_invoice(request):
    # Récupérer les données du formulaire
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    city = request.POST.get('city')
    country = request.POST.get('country')
    cartitems = request.session.get('cart', [])
    total_price = sum(item.product.formatted_selling_price for item in cartitems)

    # Rendre la vue de la facture
    return render(request, 'invoice.html', {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'city': city,
        'country': country,
        'cartitems': cartitems,
        'total_price': total_price,
    })

