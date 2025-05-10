from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages import views
from pages.views import product_detail
from pages.views import add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/', views.category, name='category'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)