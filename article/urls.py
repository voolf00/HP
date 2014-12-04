from  django.conf.urls import patterns,url

urlpatterns = patterns('',

                       url(r'^get/(\d+)', 'article.views.uArticle'),
                       url(r'^', 'article.views.uArticles'),


                       )