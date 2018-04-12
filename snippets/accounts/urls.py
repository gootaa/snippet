from django.conf.urls import url, include
from . import views as app_views
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^register/$', app_views.register, name='register'),
	url(r'^login/$',
		auth_views.LoginView.as_view(redirect_authenticated_user=True),
		name='login'),
	url(r'^logout/$', auth_views.logout_then_login, name='logout'),
	url(r'^account-settings/$', app_views.account_settings, name='account_settings'),
	url(r'^change-email/$', app_views.change_email, name='change_email'),
	url(r'^change-password/$', app_views.change_password, name='change_password'),
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
	url(r'^home/$', app_views.home, name='home'),
]