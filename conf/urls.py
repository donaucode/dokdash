from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('_accounts.urls')),
    path('', include('_global.urls')),
    path('contacts/', include('_contacts.urls')),
    path('documents/', include('_documents.urls')),
    path('tasks/', include('_tasks.urls')),
    path('trips/', include('_trips.urls')),
    path('shopping/', include('_shopping.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)