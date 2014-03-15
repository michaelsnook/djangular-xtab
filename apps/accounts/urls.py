# 2/25 http://richardtier.com/2014/02/25/django-rest-framework-user-endpoint/
from django.conf.urls import patterns, url, include
from rest_framework import routers
 
from . import api
 
router = routers.DefaultRouter()
router.register(r'accounts', api.views.UserView, 'list')
 
urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)



# 3/06 http://richardtier.com/2014/03/06/110/
#from django.conf.urls import patterns, url
#from api import views as api_views
# changed api_views to api.views
 
urlpatterns = patterns(
    '',
    url(r'^api/auth/$',
        api.views.AuthView.as_view(),
        name='authenticate')



