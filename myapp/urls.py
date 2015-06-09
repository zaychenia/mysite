__author__ = 'Olenka'

from django.conf.urls import url
from django.conf.urls import patterns

from . import views


urlpatterns = [

    url(r'^$', views.mainpage, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^mainpage', views.mainpage, name='mainpage'),
    url(r'^errpage_not_auth',views.errpage_not_auth, name='errpage_not_auth'),
    url(r'^plan_page', views.plan_page, name='plan_page'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^back_to_login', views.back_to_login, name='back_to_login'),
    # url(r'^registration', views.register, name='registration'),
    url(r'^registration', views.RegisterFormView.as_view()),
    # url(r'^registration', views.registrationForm.as_view()),
    url(r'^contacts', views.contacts),
    url(r'^info', views.info),
    url(r'^choice', views.choice),


]




