from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^posts/', views.posts_page, name='posts_page'),
    url(r'^post_details/(?P<rule_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^del_posts/(?P<rule_id>[0-9]+)/$', views.del_post, name='del_post'),

    url(r'^catalog/', views.catalog_page, name='catalog_page'),
    url(r'^course_details/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^del_course/(?P<course_id>[0-9]+)/$', views.del_course, name='del_course'),

    url(r'^facultyadv/', views.facultyadv_page, name='facultyadv_page'),
    url(r'^adv_details/(?P<adv_id>[0-9]+)/$', views.adv_detail, name='detail'),
    url(r'^adv_del/(?P<adv_id>[0-9]+)/$', views.adv_del, name='adv_del'),

]