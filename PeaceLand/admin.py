from . import models
from django.contrib import admin


############ Using admin ############
admin.site.register(models.RoomsType) #Store model in admin
admin.site.register(models.Rooms)
admin.site.register(models.BookRoom)
admin.site.register(models.Resturant)
admin.site.register(models.DessertsMenu)
admin.site.register(models.DrinkMenu)
admin.site.register(models.StartersMenu)
admin.site.register(models.MainDishesMenu)
admin.site.register(models.Amenity)
# admin.site.register(models.HotelEmployeeAttendence)
admin.site.register(models.HotelEmployee)
admin.site.register(models.AdminAddress)
admin.site.register(models.TouristPlaces)
admin.site.register(models.City)
admin.site.register(models.TourReachPlaces)
admin.site.register(models.Status)