from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',include('pages.urls')),
	path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add this line at the end of your urls.py file
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)