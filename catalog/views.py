from django.shortcuts import render

from catalog.models import Product, Contact


# Create your views here.


def get_catalog_main_page(request):
    latest_products = Product.objects.order_by('-created_date')[:5]
    for product in latest_products:
        print(f"Название: {product.name}, Цена: {product.purchase_price}")

    return render(request, 'catalog/index.html')


def get_contact_page(request):
    contacts = Contact.objects.all()
    return render(request, 'catalog/contacts.html', {'contacts': contacts})

    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
    #     print(f'Name: {name}, Email: {email}, Message: {message}')
    # return render(request, 'catalog/contacts.html')
