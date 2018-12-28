from django.conf.urls import url

from assets import views

urlpatterns = [
    url('^list/$', views.AssetListView.as_view()),
    url('^create/$', views.AssetListCreateView.as_view()),
    url('^(?P<pk>[^/]+)/$', views.AssetRUDView.as_view())
]