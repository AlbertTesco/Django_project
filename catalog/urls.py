from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import get_catalog_main_page, get_contact_page, product_detail_page

app_name = CatalogConfig.name
urlpatterns = [
                  path('', get_catalog_main_page, name='main_page'),
                  path('contacts/', get_contact_page, name='contact_page'),
                  path('product/<int:pk>/', product_detail_page, name='product_detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
