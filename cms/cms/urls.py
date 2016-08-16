from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^forum/', include('forum.urls')),
    url(r'^admin/', admin.site.urls),

    # url(r'^login/', include('forum.urls')),
]
