from django.conf.urls import url

from quote import views

urlpatterns = [
    url('^list/$', views.QuoteListView.as_view()),
    url('^create/$', views.QuoteListCreateView.as_view()),
    # url('^(?P<pk>[^/]+)/$', views.QuoteRUDView.as_view()),

]

