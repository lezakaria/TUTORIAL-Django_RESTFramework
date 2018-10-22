from django.conf.urls import url
from . import views

urlpatterns = [
  #  path('snippets/', views.snippet_list),
url(r'(?P<pk>\d+)$', views.home)
 # url(r'/<int:pk>/', views.home)
]
