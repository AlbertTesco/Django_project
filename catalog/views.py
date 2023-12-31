from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView

from catalog.forms import ContactForm, ProductForm, VersionForm, ModerProductForm, ProductFormCreate
from catalog.models import Product, Contact, Version, Category
from catalog.services import cache_category


class CatalogMainPageView(LoginRequiredMixin, ListView):
    """
    Отображение главной страницы с продуктами
    """
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['user'] = self.request.user
        context_data['categories'] = cache_category()

        return context_data


def get_products_by_category(request, category_slug):
    """Отображение продуктов по категориям"""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(request, 'catalog/products_by_category.html', {'products': products, 'category': category})


class ContactPageView(LoginRequiredMixin, ListView):
    """
    Отображение страницы с контактами
    """
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"


def create_product(request):
    """Контроллер создания нового продукта"""
    if request.method == 'POST':
        form = ProductFormCreate(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("catalog:main_page")
    else:
        form = ProductFormCreate()

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

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']

        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ModerProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ModerProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:main_page")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
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
