from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$',views.show_user, name = 'show_user'),
    url(r'^home/$',views.show_user, name = 'show_user'),
    url(r'^extractore/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^extractore/new$', views.new_user, name='new_user'),
    url(r'^extractore/user_edit$', views.new_user, name='user_edit'),
]
