from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$',views.dashbord, name = 'dashbord'),
    url(r'^home/$',views.show_user, name = 'show_user'),
    url(r'^extractore/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^extractore/new/$', views.new_user, name='new_user'),
    url(r'^extractore/user_edit/(?P<pk>[0-9]+)$$', views.new_user, name='user_edit'),
    url(r'^extractore/user_data/(?P<pk>[0-9]+)$', views.userdata, name='userdata'),
]
