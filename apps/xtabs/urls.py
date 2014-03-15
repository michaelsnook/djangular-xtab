from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover() 
from . import views
 
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apps.xtabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.OnePageAppView.as_view(), name='home'),
)
