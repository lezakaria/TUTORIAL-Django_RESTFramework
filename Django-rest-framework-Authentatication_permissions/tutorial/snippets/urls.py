from django.conf.urls import url, include
import rest_framework
from . import views

urlpatterns = [
#url(r'^api/$', include('rest_framework.urls')),
url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
url(r'^users/$', views.UserList.as_view()),
url(r'^users/(?P<pk>\d+)$',views.UserDetail.as_view()),
url(r'^$', views.SnippetList.as_view()),
url(r'^test/(?P<pk>\d+)$', views.SnippetDetail.as_view())
 # url(r'/<int:pk>/', views.home)
]
