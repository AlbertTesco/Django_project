from django.shortcuts import render

from .forms import ContactForm


# Create your views here.


def get_catalog_main_page(request):
    return render(request, 'catalog/index.html')


def get_contact_page(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f'Name: {name}, Email: {email}, Message: {message}')
    else:
        form = ContactForm()
    return render(request, 'catalog/contacts.html')
