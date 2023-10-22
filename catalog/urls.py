from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogMainPageView, ContactPageView, ProductDetailView, contact_view

app_name = CatalogConfig.name
urlpatterns = [
                  path('', CatalogMainPageView.as_view(), name='main_page'),
                  path('contacts/contact_acept/', contact_view, name='contact_acept'),
                  path('contacts/', ContactPageView.as_view(), name='contact_page'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
