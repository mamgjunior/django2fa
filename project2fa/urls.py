from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # 2fa
    path('', include(tf_urls)),
    path('account/', include('account.urls')),    
]
