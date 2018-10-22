from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$',views.home),
     url(r'(?P<pk>\d+)$', views.detail)
 # url(r'/<int:pk>/', views.home)
]
