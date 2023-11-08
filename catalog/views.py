from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView

from catalog.forms import ContactForm, ProductForm, VersionForm
from catalog.models import Product, Contact, Version


class CatalogMainPageView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'


class ContactPageView(ListView):
    """
    Отображение страницы с контактами
    """
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"


def create_product(request):
    """Контроллер создания нового продукта"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохраняем продукт
            return redirect("catalog:main_page")
    else:
        form = ProductForm()

    return render(request, 'catalog/create_product_form.html', {'form': form})


def delete_product(request, product_id):
    """Удаление продукта"""
    if request.method == 'GET':
        product = Product.objects.get(pk=product_id)
        return render(request, "catalog/delete_confirm.html", {'product': product})
    elif request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        product.delete()
        return redirect("catalog:main_page")


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:main_page")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


def contact_view(request):
    """Получение данных при обратной связи"""
    # TODO

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]
            print(name, phone, message)

    return redirect('catalog:contact_page')
