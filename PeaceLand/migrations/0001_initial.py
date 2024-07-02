# Generated by Django 5.0.6 on 2024-07-02 08:11

import PeaceLand.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phoneNo", models.BigIntegerField()),
                ("address", models.CharField(max_length=256)),
                ("emailId", models.EmailField(max_length=254)),
            ],
            options={
                "verbose_name": "HotelContact",
                "verbose_name_plural": "Hotel_Contact",
            },
        ),
        migrations.CreateModel(
            name="Amenity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("AmenityLogo", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Amenity",
                "verbose_name_plural": "Rooms_Amenity",
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
            },
        ),
        migrations.CreateModel(
            name="DessertsMenu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("DishName", models.CharField(max_length=256)),
                ("DishImage", models.ImageField(upload_to="Photo/Desserts")),
                ("DishPrice", models.IntegerField()),
                ("DishDetails", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Desserts",
                "verbose_name_plural": "Desserts Menu",
            },
        ),
        migrations.CreateModel(
            name="DrinkMenu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("DishName", models.CharField(max_length=256)),
                ("DishImage", models.ImageField(upload_to="Photo/Drink")),
                ("DishPrice", models.IntegerField()),
                ("DishDetails", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Drink Menu",
                "verbose_name_plural": "Drink_Menu",
            },
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Hotel",
                "verbose_name_plural": "Hotel_Database",
            },
        ),
        migrations.CreateModel(
            name="HotelEmployee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("EmpFstName", models.CharField(blank=True, max_length=256)),
                ("EmpLstName", models.CharField(blank=True, max_length=256)),
                ("designation", models.CharField(max_length=256)),
                ("JoinDate", models.DateTimeField()),
                ("Salary", models.CharField(max_length=256)),
                ("Address", models.CharField(max_length=256)),
                ("PhoneNo", models.BigIntegerField()),
                ("EmpImg", models.ImageField(blank=True, upload_to="EmpImg/")),
                ("ResignDate", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "HotelStaff",
                "verbose_name_plural": "HotelStaff_Details",
            },
        ),
        migrations.CreateModel(
            name="HotelEmployeeAttendence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("EmpName", models.CharField(max_length=256)),
                ("designation", models.CharField(max_length=256)),
                ("login", models.DateTimeField()),
                ("logout", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="MainDishesMenu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("DishName", models.CharField(max_length=256)),
                ("DishImage", models.ImageField(upload_to="Photo/MainDishes")),
                ("DishPrice", models.IntegerField()),
                ("DishDetails", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "MainDishes",
                "verbose_name_plural": "MainDishes Menu",
            },
        ),
        migrations.CreateModel(
            name="Resturant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("roomNo", models.IntegerField(blank=True, null=True)),
                ("phoneNo", models.BigIntegerField()),
                ("Email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("foodName", models.CharField(max_length=256)),
                ("vegName", models.CharField(max_length=256)),
                ("starterName", models.CharField(max_length=256)),
                ("breadName", models.CharField(max_length=256)),
                ("drinkName", models.CharField(max_length=256)),
                ("dessertName", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Resturant",
                "verbose_name_plural": "Resturant",
            },
        ),
        migrations.CreateModel(
            name="Rooms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("to_date", models.DateField()),
                ("adultNo", models.IntegerField()),
                ("childNo", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("room", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Rooms",
                "verbose_name_plural": "Rooms",
            },
        ),
        migrations.CreateModel(
            name="StartersMenu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("DishName", models.CharField(max_length=256)),
                ("DishImage", models.ImageField(upload_to="Photo/Starters")),
                ("DishPrice", models.IntegerField()),
                ("DishDetails", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Starters",
                "verbose_name_plural": "Starters Menu",
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "RoomStatus",
                "verbose_name_plural": "Room_Status",
            },
        ),
        migrations.CreateModel(
            name="RoomsType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("RoomName", models.CharField(max_length=256)),
                ("RoomImgM", models.ImageField(upload_to="RoomImg/")),
                ("RoomImgF", models.ImageField(upload_to="RoomImg/")),
                ("RoomImgS", models.ImageField(upload_to="RoomImg/")),
                ("RoomPrice", models.IntegerField()),
                ("RoomInfo", models.CharField(max_length=256)),
                ("Room_Total", models.IntegerField()),
                ("BookedRooms", models.IntegerField(default=0)),
                ("Room_amenities", models.ManyToManyField(to="PeaceLand.amenity")),
            ],
            options={
                "verbose_name": "TypeOfRooms",
                "verbose_name_plural": "Type_Of_Rooms",
            },
        ),
        migrations.CreateModel(
            name="BookRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("to_date", models.DateField()),
                ("adultNo", models.IntegerField()),
                ("childNo", models.IntegerField()),
                ("room_CountNo", models.IntegerField()),
                ("fstname", models.CharField(blank=True, max_length=256, null=True)),
                ("lstname", models.CharField(blank=True, max_length=256, null=True)),
                ("phoneNo", models.BigIntegerField(blank=True, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("address", models.CharField(max_length=256, null=True)),
                ("state", models.CharField(max_length=256, null=True)),
                ("city", models.CharField(max_length=256, null=True)),
                ("country", models.CharField(max_length=256, null=True)),
                ("pincode", models.IntegerField(null=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="PeaceLand.roomstype",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        default=PeaceLand.models.get_pending_status,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="PeaceLand.status",
                    ),
                ),
            ],
            options={
                "verbose_name": "BookRoom",
                "verbose_name_plural": "Rooms_Booking",
            },
        ),
        migrations.CreateModel(
            name="TourReachPlaces",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("byplane", models.CharField(max_length=256)),
                ("bybus", models.CharField(max_length=256)),
                ("bytrain", models.CharField(max_length=256)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="PeaceLand.city"
                    ),
                ),
            ],
            options={
                "verbose_name": "TourReachPlaces",
                "verbose_name_plural": "TourReachPlaces",
            },
        ),
        migrations.CreateModel(
            name="TouristPlaces",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place_headling", models.CharField(max_length=256)),
                ("places_name", models.CharField(max_length=256)),
                ("place_des", models.TextField()),
                ("place_time", models.CharField(max_length=256)),
                ("place_img", models.ImageField(upload_to="Photo/touristPlaces")),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="PeaceLand.city"
                    ),
                ),
                (
                    "place_reach",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="PeaceLand.tourreachplaces",
                    ),
                ),
            ],
            options={
                "verbose_name": "TouristPlace",
                "verbose_name_plural": "TouristPlaces",
            },
        ),
    ]
