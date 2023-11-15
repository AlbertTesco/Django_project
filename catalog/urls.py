from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogMainPageView, ContactPageView, ProductDetailView, contact_view, create_product, \
    delete_product, ProductUpdateView, ModerProductUpdateView

app_name = CatalogConfig.name
urlpatterns = [
                  path('', CatalogMainPageView.as_view(), name='main_page'),
                  path('contacts/contact_acept/', contact_view, name='contact_acept'),
                  path('contacts/', ContactPageView.as_view(), name='contact_page'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
                  path('product/create/', create_product, name='create_product'),
                  path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
                  path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
                  path('product/moder_update/<int:pk>/', ModerProductUpdateView.as_view(), name='moder_update_product'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
