from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^unity/article/', include('article.urls')),
    url(r'^unity/auth/', include('medic.urls')),

    #url(r'^get/(\d+)', 'Unity.views.article'),
    url(r'^admin/', include(admin.site.urls)),


)
