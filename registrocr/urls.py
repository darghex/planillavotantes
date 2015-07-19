from django.conf.urls import include, url
from django.contrib import admin
from registrocr.views import home

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
