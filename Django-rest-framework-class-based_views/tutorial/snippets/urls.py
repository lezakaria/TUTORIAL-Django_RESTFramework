from django.conf.urls import url
from . import views

urlpatterns = [
  #  path('snippets/', views.snippet_list),
url(r'^$', views.SnippetList.as_view()),
url(r'(?P<pk>\d+)$', views.SnippetDetail.as_view())
 # url(r'/<int:pk>/', views.home)
]
