from django.conf.urls import include, url
from django.contrib import admin
from app01.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'bootcss_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^Login$', Login),
    url(r'^regis', regis),
    url(r'^UserList$',UserList),
    url(r'^UserDetail/(?P<uid>(\d+))/$', UserDetail),
    #url(r'^Edit/(?P<uid>(\d+))/$', edit),
    url(r'^Delete/(?P<uid>(\d+))/$',Delete),   
    url(r'^testPage',testPage),

]
