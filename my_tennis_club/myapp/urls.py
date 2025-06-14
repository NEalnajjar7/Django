from django.urls import path
from . import views
from .views import CarBrandDeleteView , brand_gallery
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/gallery/', brand_gallery, name='brand_gallery'),
    path('brands/delete/<int:pk>/', CarBrandDeleteView.as_view(), name='delete_brand'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
