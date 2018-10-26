from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^course_reg/(?P<student_id>[0-9]+)/$', views.course_reg, name='course_reg'),   
]