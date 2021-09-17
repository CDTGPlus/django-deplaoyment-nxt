from django.conf.urls import url 
from basic_app import views

#Template taagging, set as global var
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other, name='other')
]