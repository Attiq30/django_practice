
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nasir/',nasir),
    path ('home/',home),
    path ('login/<user_name>/<password>',login),
    path ('signup/<user_name>/<password>',signup),
    path('login-view/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
