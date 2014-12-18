from  django.conf.urls import patterns, url

urlpatterns = patterns('',

                       url(r'^register', 'medic.views.register'),
                       url(r'^login', 'medic.views.login'),
                       url(r'^logout', 'medic.views.logout'),
                       url(r'^patient/get/(\d+)/list/(\d+)', 'medic.views.patientList'),
                       url(r'^patient/get/(\d+)/list/', 'medic.views.patientLists'),
                       url(r'^patient/get/(\d+)/addlist', 'medic.views.AddList'),
                       url(r'^patient/get/(\d+)', 'medic.views.patient'),
                       url(r'^patient/', 'medic.views.patients'),

                       # url    - - - - - /unity/auth/
                       # http://localhost:8000/unity/auth/
)