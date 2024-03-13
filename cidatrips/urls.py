from django.contrib import admin
from django.urls import path, include
from trip import urls as trip_urls
from user import urls as user_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trip/', include(trip_urls)),
    path('user/', include(user_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
