from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>\d+)/answer/$', views.answer, name='answer'),
	url(r'^add_question/$', views.add_question, name='add_question'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^profile/(?P<user_id>\d*)/$', views.user_profile, name='profile'),
	url(r'^profile/$', views.user_profile, name='profile'),
	)
