from django.conf.urls import patterns, include, url

urlpatterns = patterns('home.views',
	url(r'^', view="home_page"),
	
)
