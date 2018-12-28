from django.conf.urls import url

from hubs import views

urlpatterns = [
    url('^list/$', views.HubsListView.as_view()),
    url('^create/$', views.HubsListCreateView.as_view()),
    url('^(?P<pk>[^/]+)/$', views.HubsRUDView.as_view()),

    # url('^list/$', views.HubsListView.as_view(), name='hubs'),
    # url('^home/$', views.form, name='home'),
]
