
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', RedirectView.as_view(url='/admin'))
]
admin.site.site_header = "Gazi Tyres"
admin.site.site_title = "Transport Department"
admin.site.index_title = "Welcome to Gazi Tyres"