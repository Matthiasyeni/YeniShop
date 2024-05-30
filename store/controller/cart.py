from django.shortcuts import redirect, render 
from django.contrib import messages
from django.http.response import JsonResponse

from django.contrib.auth.decorators import login_required
from store.models import Product, Cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id )):
                    return JsonResponse({'status':'Product already in Cart'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':'Product added successfully'})
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.quantity) +" quantity available"})
            else:
                return JsonResponse({'status':'No such product found'})
        else:
            return JsonResponse({'status':'Login to Continue if you\'re register '})

    return redirect('/')

@login_required(login_url='loginpage')
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request, "store/cart.html", context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Updated successfully"})
    return redirect('/')       

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "Deleted successfully"})
    return redirect('/')


# def addtocart(request):
#     if request.method == 'POST':
#         prod_id = int(request.POST.get('product_id'))
#         product_check = Product.objects.get(id=prod_id)
#         if product_check:
#             if Cart.objects.filter(product_id=prod_id).exists():
#                 return JsonResponse({'status': 'Product already in Cart'})
#             else:
#                 prod_qty = int(request.POST.get('product_qty'))
#                 if product_check.quantity >= prod_qty:
#                     Cart.objects.create(product_id=prod_id, product_qty=prod_qty)
#                     return JsonResponse({'status': 'Product added successfully'})
#                 else:
#                     return JsonResponse({'status': f"Only {product_check.quantity} quantity available"})
#         else:
#             return JsonResponse({'status': 'No such product found'})

#     return redirect('/')

# def viewcart(request):
#     cart = Cart.objects.all()  # Obtenez tous les éléments du panier, pas seulement ceux de l'utilisateur connecté
#     context = {'cart': cart}
#     return render(request, "store/cart.html", context)

# Supprimez le décorateur @login_required pour autoriser l'accès aux utilisateurs non authentifiés
# def updatecart(request):
#     if request.method == 'POST':
#         prod_id = int(request.POST.get('product_id'))
#         if Cart.objects.filter(product_id=prod_id).exists():
#             prod_qty = int(request.POST.get('product_qty'))
#             cart = Cart.objects.get(product_id=prod_id)
#             cart.product_qty = prod_qty
#             cart.save()
#             return JsonResponse({'status': "Updated successfully"})
#     return redirect('/')       

# Supprimez le décorateur @login_required pour autoriser l'accès aux utilisateurs non authentifiés
# def deletecartitem(request):
#     if request.method == 'POST':
#         prod_id = int(request.POST.get('product_id'))
#         if Cart.objects.filter(product_id=prod_id).exists():
#             cartitem = Cart.objects.get(product_id=prod_id)
#             cartitem.delete()
#             return JsonResponse({'status': "Deleted successfully"})
#     return redirect('/')