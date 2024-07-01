from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from PeaceLand.models import *
from django.db.models import Sum,Count

# Create your views here.
def indexView(request,email):
    print("email........",email)
    current_date = datetime.now().date()
    users= User.objects.get(username=email)
    employee = HotelEmployee.objects.get(EmpFstName=users.first_name)
    
    # Print the details of the last 5 bookings
    last_five_bookings = BookRoom.objects.all().order_by('-date')[:3]
    five_user = []
    for booking in last_five_bookings:
        fst = booking.fstname
        lst = booking.lstname
        rooms = RoomsType.objects.get(RoomName=booking.room)
        img = rooms.RoomImgM
        status = booking.status
        five_user.append({
            'fst':fst,
            'lst':lst,
            'rooms':rooms,
            'img':img,
            'status':status
        })
        print(f"Name: {booking.fstname} {booking.lstname}, Booking Date: {booking.room}")
    rooms_with_booking_count = RoomsType.objects.annotate(num_bookings=Count('bookings'))
    room_count=[]
    for room in rooms_with_booking_count:
        roomName = room.RoomName
        booking = room.num_bookings
        room_count.append({
            'roomName':roomName,
            'bookings':booking
        })
        print(f"Room: {room.RoomName}, Number of Bookings: {room.num_bookings}")
    total_room_sum = RoomsType.objects.aggregate(Sum('Room_Total'))['Room_Total__sum']
    print("Total sum of Room_Total:", total_room_sum)
    room_sum = rooms_with_booking_count.aggregate(total_bookings=Sum('num_bookings'))['total_bookings']
    remain_room_sum = total_room_sum - room_sum
    print("room_count--------",room_count)
    print(employee.EmpImg)
    print("fname----------",users.first_name)
    context = {
        'current_date': current_date,
        "employee":employee,
        'room_count':room_count,
        'five_user':five_user,
        'total_room_sum':total_room_sum,
        'remain_room_sum':remain_room_sum
    }
    return render(request,"indexEmp.html",context)


def loginView(request):
    if request.method == 'POST':
        data = request.POST
        userId = data.get('Employee_Id')
        password = data.get('Password')
        if userId and password:
            user = authenticate(request, username=userId, password=password)
            if user is not None:
                request.session['username'] = userId
                users= User.objects.get(username=userId)
                print("users.........",users)
                login(request, user)
                return redirect('emp_Index', email=userId)
            else:
                return render(request, "page-login.html", {'error_message': 'Invalid Credentials'})
        else:
            return render(request, "page-login.html", {'error_message': 'Please enter both userId and password'})

    return render(request, "page-login.html")

   
def logout(request):
    del request.session['username']
    return render(request,'page-login.html')

def profileView(request,email):
    print("email........",email)
    users= User.objects.get(username=email)
    employee = HotelEmployee.objects.get(EmpFstName=users.first_name)
    print(employee.EmpImg)
    print("fname----------",users.first_name)
    context = {
        "employee":employee,
        "users" :users
    }
    return render(request,"app-profile.html",context)


def GuestListView(request, email):
    users = User.objects.get(username=email)
    employee = HotelEmployee.objects.get(EmpFstName=users.first_name)
    guestroom = BookRoom.objects.all()

    pending_status = Status.objects.get(name='Pending')
    booked_status = Status.objects.get(name='Booked')
    cancelled_status = Status.objects.get(name='Cancelled')
    refund_status = Status.objects.get(name='Refunded')

    # Query bookings based on different statuses
    pending_bookings = BookRoom.objects.filter(status=pending_status)
    booked_bookings = BookRoom.objects.filter(status=booked_status)
    cancelled_bookings = BookRoom.objects.filter(status=cancelled_status)
    refund_bookings = BookRoom.objects.filter(status=refund_status)
    context = {
        'pending_bookings': pending_bookings,
        'booked_bookings': booked_bookings,
        'cancelled_bookings': cancelled_bookings,
        'refund_bookings': refund_bookings,
        'employee': employee,
        'users': users,
        'guest':guestroom
    }
    return render(request, 'guest-list.html', context)


def guestEdit(request,id,email):
    print(id)
    print("email........",email)
    users = User.objects.get(username=email)
    queryset=BookRoom.objects.get(id=id)
    if request.method == 'POST':
        date = request.POST.get('date')
        dateTo = request.POST.get('dateTo')
        adult_no = request.POST.get('adultNo')
        child_no = request.POST.get('childNo')
        room_type_id = request.POST.get('room_type')
        fstname = request.POST.get('fstname')
        lstname = request.POST.get('lstname')
        phone_no = request.POST.get('phoneNo')
        email = request.POST.get('email')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')
        roomCount = request.POST.get('room_CountNo')
        statusPay = request.POST.get('status')
        room_type = RoomsType.objects.get(RoomName=room_type_id)  # Corrected variable name
        status_type = Status.objects.get(name=statusPay) 
        
        queryset.date=date
        queryset.to_date=dateTo
        queryset.adultNo=adult_no
        queryset.childNo=child_no
        queryset.room_CountNo = roomCount
        queryset.room=room_type  # Use room_type instead of room
        queryset.fstname=fstname
        queryset.lstname = lstname
        queryset.phoneNo=phone_no
        queryset.email=email
        queryset.address=address
        queryset.state=state
        queryset.city=city
        queryset.country=country
        queryset.pincode=pincode
        queryset.status=status_type
        queryset.save()
        return redirect('guest_list',email=users)
    statusRoom = Status.objects.all()
    rooms = RoomsType.objects.all()
    print("room",rooms)
    employee = HotelEmployee.objects.get(EmpFstName=users.first_name)
    print("-------",employee.EmpImg)
    print(rooms)
    context = {
        'update':queryset,
        'rooms':rooms,
        'users':users,
        'employee':employee,
        'status':statusRoom
    }
    return render(request,"guest-edit.html",context)


def delGuest(request,id,email):
    a = BookRoom.objects.get(id=id)
    users = User.objects.get(email=email)
    print(users.first_name)
    emails = users.username
    a.delete()
    return redirect('guest_list',email=emails)

def roomList(request,email):
    print(email)
    users = User.objects.get(username=email)
    employee = HotelEmployee.objects.get(EmpFstName=users.first_name)
    allRoom = RoomsType.objects.all()
    print("allRoom",allRoom)
    rooms_with_amenities = []
    for room in allRoom:
        amenities = room.Room_amenities.all()
        rooms_with_amenities.append({
            'room': room,
            'amenities': amenities,
        })
    context={
        'employee':employee,
        'rooms_with_amenities':rooms_with_amenities,
        'users':users
    }
    return render(request,'room-listEmp.html',context)

def roomEdit(request,email,id):
    users = User.objects.get(username=email)
    employee = HotelEmployee.objects.get(EmpFstName=users.first_name)
    allRoom = RoomsType.objects.filter(id=id)
    print("filter", allRoom)
    Room = RoomsType.objects.get(id=id)
    print("get",Room)
    bookings = BookRoom.objects.filter(room=Room)
    amenities_room = []
    for room in allRoom:
        amenities = room.Room_amenities.all()
        amenities_room.append({
            'amenities':amenities,
            'price':room.RoomPrice
        })
    prices = [details['price'] for details in amenities_room][0]
    print("---------",prices)
    context={
        'employee':employee,
        'users':users,
        'allRoom':allRoom,
        'amenities_room':amenities_room,
        'bookings':bookings,
        'price':prices
    }
    return render(request,'room-edit.html',context)

def resturantBill(request,email):
    users = User.objects.get(username=email)
    employee = HotelEmployee.objects.get(EmpFstName=users.first_name)
    if request.method == 'POST':
        name = request.POST.get('name')
        FoodName = request.POST.get('FoodName')
        VegName = request.POST.get('VegName')
        StarterName = request.POST.get('StarterName')
        email = request.POST.get('email')
        address = request.POST.get('address')
        DessertName = request.POST.get('DessertName')
        phoneNo = request.POST.get('phoneNo')
        RoomNo = request.POST.get('RoomNo')
        BreadName = request.POST.get('BreadName')
        DrinkName = request.POST.get('DrinkName')       
        Resturant.objects.create(
            drinkName=DrinkName,
            breadName=BreadName,
            roomNo=RoomNo,
            phoneNo=phoneNo,
            dessertName=DessertName, 
            address = address,
            Email=email,
            starterName=StarterName,
            vegName = VegName,
            foodName=FoodName,
            name=name
        )
        # return redirect('restaurant',email=email) 
    context={
        'employee':employee,
        'users':users
     }
    return render(request,'resturant.html',context)