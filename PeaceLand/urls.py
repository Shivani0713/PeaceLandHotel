"""
URL configuration for HotelMgnt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from Paradise.admin import hotel_admin_site

# Instantiate the custom admin site


urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("admin/", hotel_admin_site.urls), #remove hotel site
    path("index",showIndex, name='show_Index'),
    path("room-list",RoomListIndex),
    path("room-details-booking/<int:id>",RoomBookingIndex),
    path("restaurant",RestaurantIndex),
    path("menu-of-the-day",MenuDayIndex),
    path("about",AboutIndex),
    path("contacts",ContactIndex),
    path("places",PlaceIndex),
    path("place-details/<int:id>",PlaceDetails, name="place-details"),
    path("room-book/<int:id>/<str:email>/",RoomBook, name='book_room'),
    path("room-book",RoomBook, name='book_room'),
    path('send_admin_booking_email/', send_admin_notification_email, name='send_admin_booking_email'),
    path('send_user_booking_email/', send_user_confirmation_email, name='send_user_booking_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin.site.index_title = "PEACE_LAND"
# admin.site.site_header ="PEACE_LAND ADMIN"
# admin.site.site_title = "PEACE_LAND ADMIN"
