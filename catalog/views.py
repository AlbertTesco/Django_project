from django.shortcuts import render

from catalog.models import Product, Contact


# Create your views here.


def get_catalog_main_page(request):
    products = Product.objects.all()[:101]
    context = {
        "products": products
    }
    return render(request, 'catalog/index.html', context)


def get_contact_page(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'catalog/contacts.html', context)


def product_detail_page(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
