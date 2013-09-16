from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from searchExample import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haystackExample.views.home', name='home'),
    # url(r'^haystackExample/', include('haystackExample.foo.urls')),
    #url(r'^$', views.notes, name='notes'),
    #url(r'^search/', include('haystack.urls')),
    url(r'^', include('haystack.urls')),
    url(r'^(?P<pk>\d+)$', views.note, name='note'),
    
    #this has to be commented out for the admin to work
    #I think it has something to do with running the query on the home page
    url(r'^', views.notes, name='notes'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
