from django.conf.urls import url
from Blood_app import views

app_name = 'Blood_app'

urlpatterns =[
    url(r'^$',views.index,name = 'index'),
    url(r'^signup/$',views.Sign_up,name='signup')
    ]
