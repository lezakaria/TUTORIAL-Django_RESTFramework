from django.conf.urls import url, include
from django.contrib import admin
from . import views
import rest_framework

urlpatterns=[
   # url(r'', views.home),
    url(r'^admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^', include('snippets.urls'))
]