from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
# Create your models here.

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    AmenityLogo = models.CharField(max_length=256)
    class Meta:
        verbose_name = ("Amenity")
        verbose_name_plural = ("Rooms_Amenity") #Admin Shows
    def __str__(self):
        return self.name
    
    
class RoomsType(models.Model):
    RoomName = models.CharField(max_length=256)
    RoomImgM = models.ImageField(upload_to="RoomImg/")
    RoomImgF = models.ImageField(upload_to="RoomImg/")
    RoomImgS = models.ImageField(upload_to="RoomImg/")
    RoomPrice = models.IntegerField()
    RoomInfo = models.CharField(max_length=256) 
    Room_amenities = models.ManyToManyField(Amenity)
    Room_Total = models.IntegerField()
    BookedRooms = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = ("TypeOfRooms")
        verbose_name_plural = ("Type_Of_Rooms") #Admin Shows
        
    def __str__(self):
        return f"{self.RoomName}"
    
    
class Rooms(models.Model):
    date = models.DateField()
    to_date = models.DateField()
    adultNo = models.IntegerField()
    childNo = models.IntegerField()
    email = models.EmailField()
    room = models.CharField(max_length=256)
    
    class Meta:
        verbose_name = ("Rooms")
        verbose_name_plural = ("Rooms") #Admin Shows
        
        
class Status(models.Model):
    name = models.CharField(max_length=256)
    class Meta:
        verbose_name = ("RoomStatus")
        verbose_name_plural = ("Room_Status")

    def __str__(self):
        return self.name
def get_pending_status():
    return Status.objects.get(name='Pending')

class BookRoom(models.Model):
    date = models.DateField()
    to_date = models.DateField()
    adultNo = models.IntegerField()
    childNo = models.IntegerField() 
    room_CountNo = models.IntegerField()
    room = models.ForeignKey(RoomsType, on_delete=models.CASCADE,related_name='bookings')
    fstname = models.CharField(max_length=256,null=True,blank=True)
    lstname = models.CharField(max_length=256,null=True,blank=True)
    phoneNo = models.BigIntegerField(null=True,blank=True)  
    email = models.EmailField(null=True)
    address = models.CharField(max_length=256,null=True)
    state = models.CharField(max_length=256,null=True)
    city = models.CharField(max_length=256,null=True)
    country = models.CharField(max_length=256,null=True)
    pincode = models.IntegerField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,default=get_pending_status)
    
    class Meta:
        verbose_name = ("BookRoom") #Same As Model
        verbose_name_plural = ("Rooms_Booking") #Admin Shows
        
    def __str__(self):
        return f"{self.fstname}"" "f"{self.lstname}"  # Adjust this based on your model fields
    
    def save(self, *args, **kwargs):
        if not self.pk:  # This is a new instance
            booked_rooms = int(self.room.BookedRooms) if int(self.room.BookedRooms) is not None else 0
            room_count = int(self.room_CountNo)
            room_total = int(self.room.Room_Total)
            if booked_rooms + room_count <= room_total:
                self.room.BookedRooms = booked_rooms + room_count
                self.room.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        booked_rooms = int(self.room.BookedRooms) if self.room.BookedRooms is not None else 0
        room_count = int(self.room_CountNo)

        self.room.BookedRooms = booked_rooms - room_count
        self.room.save()
        super().delete(*args, **kwargs)


@receiver(post_migrate)
def create_pending_status(sender, **kwargs):
    if sender.name == 'Paradise':
        Status.objects.get_or_create(name='Pending')
           

    
class StartersMenu(models.Model):
    DishName = models.CharField(max_length=256)
    DishImage = models.ImageField(upload_to="Photo/Starters")
    DishPrice = models.IntegerField()
    DishDetails = models.CharField(max_length=256)
    class Meta:
        verbose_name = ("Starters")
        verbose_name_plural = ("Starters Menu") #Admin Shows
    def __str__(self):
        return self.DishName
    
    
class MainDishesMenu(models.Model):
    DishName = models.CharField(max_length=256)
    DishImage = models.ImageField(upload_to="Photo/MainDishes")
    DishPrice = models.IntegerField()
    DishDetails = models.CharField(max_length=256)
    class Meta:
        verbose_name = ("MainDishes") #Same As Model
        verbose_name_plural = ("MainDishes Menu") #Admin Shows
    def __str__(self):
        return self.DishName

class DessertsMenu(models.Model):
    DishName = models.CharField(max_length=256)
    DishImage = models.ImageField(upload_to="Photo/Desserts")
    DishPrice = models.IntegerField()
    DishDetails = models.CharField(max_length=256)
    class Meta:
        verbose_name = ("Desserts") #Same As Model
        verbose_name_plural = ("Desserts Menu") #Admin Shows
    def __str__(self):
        return self.DishName
    
class DrinkMenu(models.Model):
    DishName = models.CharField(max_length=256)
    DishImage = models.ImageField(upload_to="Photo/Drink")
    DishPrice = models.IntegerField()
    DishDetails = models.CharField(max_length=256)
    class Meta:
        verbose_name = ("Drink Menu") #Same As Model
        verbose_name_plural = ("Drink_Menu") #Admin Shows
    def __str__(self):
        return self.DishName
    
    
class Hotel(models.Model):
    title = models.CharField(max_length=256)
    
    class Meta:
        verbose_name = ("Hotel")
        verbose_name_plural = ("Hotel_Database") #Admin Shows
    
    def __str__(self):
        return self.title
    
class HotelEmployeeAttendence(models.Model):
    EmpName = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    login = models.DateTimeField()
    logout = models.DateTimeField()
    
    
class HotelEmployee(models.Model):
    title = models.CharField(max_length=256)
    EmpFstName = models.CharField(max_length=256,blank=True)
    EmpLstName = models.CharField(max_length=256,blank=True)
    designation = models.CharField(max_length=256)
    JoinDate = models.DateTimeField()
    Salary = models.CharField(max_length=256)
    Address = models.CharField(max_length=256)
    PhoneNo = models.BigIntegerField()  
    EmpImg= models.ImageField(upload_to="EmpImg/",blank=True)
    ResignDate = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name = ("HotelStaff")
        verbose_name_plural = ("HotelStaff_Details") #Admin Shows
    
    def __str__(self):
        return self.title
    
   
class AdminAddress(models.Model):
    phoneNo = models.BigIntegerField()
    address = models.CharField(max_length=256)
    emailId = models.EmailField()
    
    class Meta:
        verbose_name = ("HotelContact")
        verbose_name_plural = ("Hotel_Contact") #Admin Shows
    
    def __str__(self):
        return self.address


class City(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.name

class TourReachPlaces(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    byplane = models.CharField(max_length=256)
    bybus = models.CharField(max_length=256)
    bytrain = models.CharField(max_length=256)

    class Meta:
        verbose_name = ("TourReachPlaces")
        verbose_name_plural = ("TourReachPlaces")

    def __str__(self):
        return f"{self.city.name}: Plane: {self.byplane}, Bus: {self.bybus}, Train: {self.bytrain}"

class TouristPlaces(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    place_headling = models.CharField(max_length=256)
    places_name = models.CharField(max_length=256)
    place_des = models.TextField()
    place_time = models.CharField(max_length=256)
    place_reach = models.ForeignKey(TourReachPlaces, on_delete=models.CASCADE)
    place_img = models.ImageField(upload_to="Photo/touristPlaces")

    class Meta:
        verbose_name = ("TouristPlace")
        verbose_name_plural = ("TouristPlaces")

    def __str__(self):
        return self.places_name



class Resturant(models.Model):
    name = models.CharField(max_length=256)
    roomNo = models.IntegerField(null=True,blank=True)
    phoneNo = models.BigIntegerField()  
    Email =  models.EmailField()
    address = models.TextField()
    foodName=models.CharField(max_length=256)
    vegName = models.CharField(max_length=256)
    starterName = models.CharField(max_length=256)
    breadName = models.CharField(max_length=256)
    drinkName = models.CharField(max_length=256)
    dessertName = models.CharField(max_length=256)
    class Meta:
        verbose_name = ("Resturant")
        verbose_name_plural = ("Resturant") #Admin Shows
    def __str__(self):
        return self.name
    
    