from django.shortcuts import redirect, render 
from .models import *
from django.contrib import messages
from django.http.response import JsonResponse
from .forms import ContactUserForm
from django.core.mail import send_mail
from django.utils.translation import gettext as _


from django.http import HttpResponse, HttpResponseRedirect
from reportlab.pdfgen import canvas

# from django.http import JsonResponse
from django.utils.translation import activate
from django.utils import translation
from django.http import HttpResponse


# Create your views here.
def home(request):
    trending_products = Product.objects.filter(trending=1)
    context = {'trending_products':trending_products}
    return render(request, "store/index.html", context)

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "store/collections.html", context)



def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(Category__slug=slug)
        category = Category.objects.filter(slug=slug).first() 
        context = {'products':products, 'category':category}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect("collections")


# def collectionsview(request, slug):
#     if Category.objects.filter(slug=slug, status=0).exists():
#         products = Product.objects.filter(Category__slug=slug, status=0)
#         category = Category.objects.filter(slug=slug, status=0).first() 
#         context = {'products': products, 'category': category}
#         return render(request, "store/products/index.html", context)
#     else:
#         messages.warning(request, "No such category found")
#         return redirect("collections")



def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products =  Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "No such products found")
            return redirect("collections")
    else:
        messages.error(request, "No such products found")
        return redirect("collections")
    return render(request, "store/products/view.html", context)


def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productsList = list(products)
    return JsonResponse(productsList, safe=False)

def searchproduct(request):
    if request.method =="POST":
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()

            if product:
                return redirect('collections/'+product.Category.slug+'/'+product.slug )
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))



def contact(request):
    if request.method == 'POST':
        fm = ContactUserForm(request.POST)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.user = request.user
            instance.save()

            # Envoyer un e-mail au destinataire
            subject = 'New message from contact form'
            message = f"""
            First Name: {instance.firstname}
            Last Name: {instance.name}
            Email: {instance.email}
            Phone: {instance.phone}
            Subject: {instance.subject}
            City: {instance.city}
            Country: {instance.country}
            """
            sender_email = 'yenishop75@gmail.com'  # Votre adresse e-mail Gmail
            recipient_email = 'yenishop75@gmail.com'  # Adresse e-mail du destinataire

            # Envoyer un e-mail au destinataire
            send_mail(subject, message, sender_email, [recipient_email])

            # Envoyer un message de remerciement à l'utilisateur
            thank_you_subject = 'Thank you for contacting us!'
            thank_you_message = 'Thank you for contacting us. We will respond to your message shortly.'
            send_mail(thank_you_subject, thank_you_message, sender_email, [instance.email])

            messages.success(request, "Message received! Thank You:)")
            return render(request, "store/index.html")

    else:
        fm = ContactUserForm()
    return render(request, 'contact_form.html', {'form': fm})

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:  # Vérifie si l'adresse e-mail est fournie
            # Enregistrez l'adresse e-mail dans la base de données
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, "You have successfully subscribed to the newsletter. Thank you!")
        else:
            messages.error(request, "Please provide an email address.")
    return redirect("/")


def generate_invoice(request):
    # Traitement des données du formulaire (à adapter selon votre modèle de données)
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    city = request.POST.get('city')
    country = request.POST.get('country')
    total_price = ...  # Calculer le prix total de la commande

    # Génération de la facture (utilisation de ReportLab pour créer un PDF)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 750, "Facture de paiement")
    p.drawString(100, 730, f"Nom: {first_name} {last_name}")
    # Ajouter d'autres détails de la facture
    p.showPage()
    p.save()

    return response


def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /login/",
        "Disallow: /register/",
        "Disallow: /password_reset/",
        "Sitemap: https://www.votresite.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")




# def your_view(request):
#     current_year = YourModel().current_year()  # Obtenez l'année actuelle à partir de votre modèle
#     return render(request, 'your_template.html', {'current_year': current_year})