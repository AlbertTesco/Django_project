from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from catalog.forms import ContactForm
from catalog.models import Product, Contact


class CatalogMainPageView(ListView):
    """
    Отображение главной страницы с товарами
    """
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "products"
    queryset = Product.objects.all()[:101]
    # FBV
    # def get_catalog_main_page(request):
    #     products = Product.objects.all()[:101]
    #     context = {
    #         "products": products
    #     }
    #     return render(request, 'catalog/index.html', context)


class ContactPageView(ListView):
    """
    Отображение страницы с контактами
    """
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"
    # FBV
    # def get_contact_page(request):
    #     contacts = Contact.objects.all()
    #     context = {
    #         "contacts": contacts
    #     }
    #     return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"
    # FBV
    # def product_detail_page(request, pk):
    #     product = Product.objects.get(id=pk)
    #     return render(request, 'catalog/product_detail.html', {'product': product})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]
            print(name, phone, message)

    return redirect('catalog:contact_page')
