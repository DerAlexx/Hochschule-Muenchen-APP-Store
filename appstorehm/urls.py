from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('api/apps/', include('app_product.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('test2/', views.test2),
    path('test2/login', views.login_),
    path('test2/logout', views.login_)
]