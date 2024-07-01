"""HotelPeaceLand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from PeaceLand.views import *

urlpatterns = [
    path("Emplogin",loginView, name="emp_login"),
    path("Empindex/<str:email>",indexView, name='emp_Index'),
    path("Profileindex/<str:email>",profileView, name='app_profile'),
    path("Guest_list/<str:email>",GuestListView,name="guest_list"),
    path("Guest_edit/<str:email>/<int:id>",guestEdit,name="guest_edit"),
    path("Guest_list/<str:email>/<int:id>",delGuest,name="guest_del"),
    path("Room_list/<str:email>",roomList,name="room_list"),
    path("Room_edit/<str:email>/<int:id>",roomEdit,name="rooms_edit"),
    path("EmpLog",logout, name="emp_logout"),
    path("Rest/<str:email>",resturantBill,name="restaurant"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
