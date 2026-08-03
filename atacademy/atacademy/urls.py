from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve
from core.admin import admin_site
from core.admin_views import (
    export_enquiries, export_callbacks, export_brochures,
    export_recruiters, export_all
)

urlpatterns = [
    path('admin/', admin_site.urls),
    path('admin/export/', export_all, name='export_all'),
    path('admin/export/enquiries/', export_enquiries, name='export_enquiries'),
    path('admin/export/callbacks/', export_callbacks, name='export_callbacks'),
    path('admin/export/brochures/', export_brochures, name='export_brochures'),
    path('admin/export/recruiters/', export_recruiters, name='export_recruiters'),
    path('', include('core.urls')),
]

# Always serve media files (uploaded images) regardless of DEBUG
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
