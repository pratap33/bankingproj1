from django.conf.urls import url
from userapp1.views import Homepage,Loginpage,Loginpage1,Showpage
from . import views
app_name='userapp1'
urlpatterns=  [
    url(r'^homepage$',Homepage.as_view()),
    url(r'^loginpage1$',Loginpage1.as_view()),
    url(r'^loginpage$',Loginpage.as_view()),
    url(r'^showpage$',Showpage.as_view()),
    url(r'^insert$',views.insert, name='insert'),
    url(r'^function$',views.function, name='function'),
    url(r'^split$',views.split,name='split'),

]