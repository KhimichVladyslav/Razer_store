from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls', namespace='basket')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('', include('store.urls', namespace='store')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
