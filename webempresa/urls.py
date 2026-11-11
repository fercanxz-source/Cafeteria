from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # <--- Rutas principales gestionadas por core
    path('blog/', include('blog.urls')), # <--- Rutas del blog
    path('services/', include('services.urls')),
    path('social/', include('social.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)