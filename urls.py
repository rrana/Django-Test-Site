from django.conf.urls.defaults import patterns, include, url
from mysite.views import hello
from mysite.views import current_datetime
from mysite.views import hours_ahead
from mysite.views import display_meta
from mysite.books import views
from mysite.contact.views import contact
from mysite.views import test

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     ('^hello/$', hello),
     ('^time/$', current_datetime),
     (r'^time/plus/(\d{1,2})/$', hours_ahead),
     (r'^meta/$', display_meta),
     (r'^search/$', views.search),                
     (r'^contact/$', contact),
     (r'^test/$', test),

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
