from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),  
    path('', include('apiTask.urls')),
    path('', include('myapp.urls')),
    path('', include('accounts.urls')),
]
