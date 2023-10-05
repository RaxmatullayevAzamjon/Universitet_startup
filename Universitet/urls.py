
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bosh_sahifa),
    path('ustozlar/', ustozlar),
    path('fanlar/', fan),
    path('yonalish/', yonalish),
    path('ustoz_update/<int:son>/', ustoz_update),
    path('ustoz_ochir/<int:son>/', ustoz_ochir),
    path('yonalish_ochir/<int:son>/', yonalish_ochir),
    path('fan_ochir/<int:son>/', fan_ochir),
    path('fan_update/<int:son>/', fan_update),
    path('yonalish_update/<int:son>/', yonalish_update),
]
