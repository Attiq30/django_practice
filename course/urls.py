
from django.contrib import admin
from django.urls import path
from course.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nasir/',nasir),
    path ('home/',home),
    path ('login/<user_name>/<password>',login),
    path ('signup/',signup)
]
