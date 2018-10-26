from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^approve/(?P<student_id>[0-9]+)/$',views.approve,name='approve'),
    url(r'^disapprove/(?P<student_id>[0-9]+)/$',views.approve,name='disapprove'),
]