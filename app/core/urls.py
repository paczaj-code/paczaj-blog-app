
from django.contrib import admin
from django.urls import path, include
from terminology import urls
from blog import urls
from category import urls
from practice import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('category.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('terminology.urls')),
    path('api/', include('practice.urls')),
]
