from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import views as page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_views.home, name='home'),
    path('about/', page_views.about, name='about'),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('messages/', include('messaging.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
