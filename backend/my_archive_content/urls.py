from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'core.views.page_not_found'
handler500 = 'core.views.page_error'

urlpatterns = [
    path('', include('content.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
