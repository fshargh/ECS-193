"""ecs193 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^stebbins/', 'stebbins.views.oldindex'),
    url(r'^/$', include('stebbins.urls', namespace="stebbins")),
    url(r'', include('stebbins.urls', namespace="stebbins")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^accounts/login/$', 'stebbins.views.login'),
    url(r'^accounts/logout/$', 'stebbins.views.logout'),
    url(r'^accounts/loggedin/$', 'stebbins.views.loggedin'),
    url(r'^accounts/profile/$', 'stebbins.views.profile'),
    url(r'^accounts/invalid/$', 'stebbins.views.invalid_login'),
    url(r'^accounts/register/$', 'stebbins.views.register_user'),
    url(r'^accounts/register_success/$', 'stebbins.views.register_success'),
    url(r'^accounts/internalLogin/$', 'stebbins.views.internalLogin'),
     url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset', kwargs={'template_name' : 'password_reset.html'}),
    url(r'^accounts/password_reset_done/$', 'django.contrib.auth.views.password_reset_done', kwargs={'template_name' : 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^accounts/password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', kwargs={'template_name' : 'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^accounts/activate/(?P<userName>\w{1,50})/(?P<activation_key>\w{1,50})/$', 'stebbins.views.activate'),
	url(r'^web-players-status/$', 'stebbins.views.webLoggedIn'),
    url(r'^game-players-status/$', 'stebbins.views.internalLoggedIn'),
    url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset'),
    url(r'^accounts/password_reset_done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^accounts/password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^accounts/password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete',  name='password_reset_complete'),
    url(r'^downloads/$', 'stebbins.views.downloads'),
    url(r'^accounts/edit/$', 'stebbins.views.edit_profile'),
    url(r'^accounts/edit_profile_success/$', 'stebbins.views.edit_profile_success'),
    url(r'^accounts/change_password/$', 'stebbins.views.change_password'),
    url(r'^accounts/change_password_success/$', 'stebbins.views.change_password_success'),
    url(r'^compose_success/$', 'stebbins.views.compose_success'),    
    url(r'^send_something/$', 'stebbins.views.send_something'),
    url(r'^forum/forum/(\d+)/$', 'forum.views.forum'),
    url(r'^forum/thread/(\d+)/$', 'forum.views.thread'), 
    url(r'^forum/post/(new_thread|reply)/(\d+)/$', 'forum.views.post'),
    url(r'^forum/reply/(\d+)/$', 'forum.views.reply'),
    url(r'^forum/profile/(\d+)/$', 'forum.views.profile'),
    url(r'^forum/new_thread/(\d+)/$', 'forum.views.new_thread'),
    url(r'^forum/$', 'forum.views.main'),
    url(r'^accounts/internalLogin/$', 'stebbins.views.internalLogin'),
    url(r'^accounts/internalLogout/$', 'stebbins.views.internalLogout'),
    url(r'^accounts/internalUpdate/$', 'stebbins.views.internalUpdate'),
     url(r'^accounts/friends/$', 'stebbins.views.friends'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)