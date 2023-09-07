from django.contrib import admin
from django.urls import path, include
from navigator.handler_exc import errors_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('city/', include('geo.urls')),
    path('shop/', include('shops.urls'))
]

handler500 = errors_handler
handler404 = errors_handler

