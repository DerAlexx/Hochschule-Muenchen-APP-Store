from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restService.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    #re_path('.*', TemplateView.as_view(template_name='index.html') )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)