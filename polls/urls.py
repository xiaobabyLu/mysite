from django.conf.urls import url
from polls import views,search,search2
from TestModel import testdb

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index1'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', views.login, name='login'),

    url(r'^logout/$', views.logout, name='logout'),

    url(r'^input/$', views.form_input, name='input'),

    url(r'^testdb/$',testdb.testdb,name='testdb'),

    url(r'^search/$',search.search,name='search'),

    url(r'^search-post/$', search2.search_post, name='search-post'),

    url(r'^search_form/$', search.search_form, name='search_form'),

    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),

    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(),name='results'),

    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
