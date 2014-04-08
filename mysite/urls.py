#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from mysite.views import hello
from mysite.views import my_homepage
from mysite.views import current_datetime
from mysite.views import hours_ahead
from books import views

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
# test
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^$', hello),
     url(r'^hello/$', hello),
     url(r'^time/$', current_datetime),
     url(r'^date/$', current_datetime),
     url(r'^search-form/$', views.search_form),
     url(r'^search/$', views.search),
     url(r'^time/plus/(\d{1,2})/$', hours_ahead),
#     url(r'^admin/', include(admin.site.urls)),

)
