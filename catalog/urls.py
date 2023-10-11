from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import get_catalog_main_page, get_contact_page

app_name = 'catalog'

urlpatterns = [
                  path('', get_catalog_main_page, name='main_page'),
                  path('contacts/', get_contact_page, name='contact_page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)