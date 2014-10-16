from django.conf.urls import patterns, include, url
from ask import views
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',views.home),
    url(r'^home/$', views.home),
    url(r'^home/(?P<str1>\w+)/$', views.home),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/profile/$', views.home),
    url(r'^accounts/profile/(?P<username_id>\d+)/$', views.profile),
    url(r'^add/question/$', views.add_question),
    url(r'^add/answer/(?P<question_id>\d+)/(?P<str2>\w+)/$', views.add_answer),
    url(r'^add/answer/(?P<question_id>\d+)/$', views.add_answer),
    url(r'^about/$', views.about),
    url(r'^add/user/$', views.add_user),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',views.error404),
)
