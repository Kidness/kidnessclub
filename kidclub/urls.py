from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^clients/$', 'club.views.index'),
     url(r'^init/$', 'club.views.init'),
	# Examples:
    # url(r'^$', 'kidclub.views.home', name='home'),
    # url(r'^kidclub/', include('kidclub.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
