from django.contrib import admin
from django.urls import path, include
from trip import urls as trip_urls
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trip/', include(trip_urls)),
    path('user/', include(user_urls)),

]
