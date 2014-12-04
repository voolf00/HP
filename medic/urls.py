from  django.conf.urls import patterns,url

urlpatterns = patterns('',

                       url(r'^login', 'medic.views.login'),
                       url(r'^logout', 'medic.views.logout'),



                       )