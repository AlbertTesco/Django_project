from django.conf import settings
from django.conf.urls.static import static

from blog.apps import BlogConfig

app_name = BlogConfig.name
urlpatterns = [

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)