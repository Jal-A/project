from django.contrib import admin
from django.urls import path

from website.views import home, about,gallery,login,signup
from accounts.views import login_view
/* urlpatterns = [
    path('',views.index)
] */

urlpatterns = [

    path('',home,name='home'),

    path(r'^about/$', views.about),
    path(r'^gallery/$', views.gallery),
    path(r'^login/$', views.login),
    path(r'^signup/$', views.signup),
    path('accounts/login/',login_view)
