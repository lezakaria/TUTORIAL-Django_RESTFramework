from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns=[
   # url(r'', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'', include('snippets.urls'))
]