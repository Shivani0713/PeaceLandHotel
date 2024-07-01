from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PeaceLand.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
from django.utils.html import strip_tags
from fpdf import FPDF
import qrcode
from django.core.mail import EmailMessage
import os
from django.conf import settings
import base64

def showIndex(request):
    if request.method == 'POST':
        date = request.POST.get('datepicker')
        room_type = request.POST.get('room_type')
        adults = request.POST.get('adults_booking')
        childs = request.POST.get('childs_booking')
        dateTo = request.POST.get('datepickerTo')
        email = request.POST.get('emailId')

        # Check for empty fields if necessary
        if not date or not room_type or not adults or not childs or not dateTo or not email:
            # Handle error: return an error message or render the form again with an error
            return render(request, "index.html", {'error': 'All fields are required.'})

        # Store data in session
        room = Rooms.objects.create(date=date, adultNo=adults, childNo=childs, room=room_type, to_date=dateTo, email=email)
        request.session['room_id'] = room.id
        request.session['room_email'] = room.email

        # Redirect to the same view to avoid re-submission of form data
        return redirect('book_room', id=room.id, email=email)

    room_id = request.session.get('room_id')
    room_email = request.session.get('room_email')

    rooms = RoomsType.objects.all()
    contact = AdminAddress.objects.all()
    context = {
        'rooms': rooms,
        'room_id': room_id,
        'room_email': room_email,
        'contacts':contact
    }
    return render(request, "index.html", context)


def RoomListIndex(request):
    if request.method == 'POST':
        date = request.POST.get('datepicker')
        room_type = request.POST.get('room_type')
        adults = request.POST.get('adults_booking')
        childs = request.POST.get('childs_booking')
        dateTo = request.POST.get('datepickerTo')
        email = request.POST.get('emailId')

        # Check for empty fields if necessary
        if not date or not room_type or not adults or not childs or not dateTo or not email:
            # Handle error: return an error message or render the form again with an error
            return render(request, "index.html", {'error': 'All fields are required.'})

        # Store data in session
        room = Rooms.objects.create(date=date, adultNo=adults, childNo=childs, room=room_type, to_date=dateTo, email=email)
        request.session['room_id'] = room.id
        request.session['room_email'] = room.email

        # Redirect to the same view to avoid re-submission of form data
        return redirect('book_room', id=room.id, email=email)

    room_id = request.session.get('room_id')
    room_email = request.session.get('room_email')
    fst_room = RoomsType.objects.all()[0]
    fst_amenities =  fst_room .Room_amenities.all()[:2]
    snd_room = RoomsType.objects.all()[1]
    snd_amenities =  snd_room .Room_amenities.all()[:2]
    trd_room = RoomsType.objects.all()[2]
    trd_amenities =  trd_room .Room_amenities.all()[:2]
    frt_room = RoomsType.objects.all()[3]
    frt_amenities =  frt_room .Room_amenities.all()[:2]
    contact = AdminAddress.objects.all()
    rooms = RoomsType.objects.all()
    context={
        "fst_room":fst_room,
        "snd_room":snd_room,
        "trd_room":trd_room,
        "frt_room":frt_room,
        'fst_amenities':fst_amenities,
        'snd_amenities':snd_amenities,
        'trd_amenities':trd_amenities,
        'frt_amenities':frt_amenities,
        'contacts':contact,
        'rooms':rooms
    }
    return render(request,"room-list.html",context)

def RoomBookingIndex(request,id):
    if request.method == 'POST':
        date = request.POST.get('datepicker')
        room_type = request.POST.get('room_type')
        adults = request.POST.get('adults_booking')
        childs = request.POST.get('childs_booking')
        dateTo = request.POST.get('datepickerTo')
        email = request.POST.get('emailId')

        # Check for empty fields if necessary
        if not date or not room_type or not adults or not childs or not dateTo or not email:
            # Handle error: return an error message or render the form again with an error
            return render(request, "index.html", {'error': 'All fields are required.'})

        # Store data in session
        room = Rooms.objects.create(date=date, adultNo=adults, childNo=childs, room=room_type, to_date=dateTo, email=email)
        request.session['room_id'] = room.id
        request.session['room_email'] = room.email

        # Redirect to the same view to avoid re-submission of form data
        return redirect('book_room', id=room.id, email=email)

    room_id = request.session.get('room_id')
    room_email = request.session.get('room_email')
    other_rooms = RoomsType.objects.exclude(id=id)
    roomType = get_object_or_404(RoomsType, id=id)
    amenities = roomType.Room_amenities.all()
    contact = AdminAddress.objects.all()
    rooms = RoomsType.objects.all()
    context={
        "roomType":roomType,
        'amenities': amenities,
        'other_rooms': other_rooms,
        'contacts':contact,
        'rooms':rooms
    }
    return render(request,"room-details-booking.html",context)


def RoomBook(request,id=None,email=None):
    bookings = None
    if id is not None and email is not None:
        try:
            bookings = Rooms.objects.get(id=id, email=email)
        except Rooms.DoesNotExist:
            bookings = None
    
    if request.method == 'POST':
        date = request.POST.get('datepicker')
        dateTo = request.POST.get('datepickerTo')
        adult_no = request.POST.get('adults_booking')
        child_no = request.POST.get('childs_booking')
        room_type_id = request.POST.get('room_type')
        fstname = request.POST.get('name_contact')
        lstname = request.POST.get('lastname_contact')
        phone_no = request.POST.get('phone_contact')
        email = request.POST.get('email_contact')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')
        roomCount = request.POST.get('room_count')
        room_type = RoomsType.objects.get(RoomName=room_type_id)  # Corrected variable name
        
        book_room = BookRoom.objects.create(
            date=date,
            to_date=dateTo,
            adultNo=adult_no,
            childNo=child_no,
            room_CountNo = roomCount,
            room=room_type,  # Use room_type instead of room
            fstname=fstname,
            lstname = lstname,
            phoneNo=phone_no,
            email=email,
            address=address,
            state=state,
            city=city,
            country=country,
            pincode=pincode
        )
        payment_url = 'https://example.com/payment'  # Replace with actual payment URL
        pdf_path = generate_booking_pdf(book_room, payment_url)
        
        # Send confirmation email with PDF
        book_room = BookRoom.objects.get(id=id)
        pdf_path = os.path.join(settings.MEDIA_ROOT, f'booking_{fstname}{lstname}.pdf')
        print("___________",pdf_path)
        send_user_confirmation_email(request,book_room, pdf_path)
        
        return redirect('show_Index') 
    room_numbers = range(1, 101)
    rooms = RoomsType.objects.all()
    contact = AdminAddress.objects.all()
    context = {
        "rooms": rooms,
        'bookings': bookings,
        'room_numbers':room_numbers,
        'contacts': contact
    }
    send_admin_notification_email(context)
    # send_user_confirmation_email()
    return render(request, "RoomBooking.html", context)


def RestaurantIndex(request):
    starter = StartersMenu.objects.all()
    maincourse = MainDishesMenu.objects.all()
    dessert = DessertsMenu.objects.all()
    drinks = DrinkMenu.objects.all()
    contact = AdminAddress.objects.all()
    context={
        's': starter,
        'm': maincourse,
        'ds': dessert,
        'dr':drinks,
        'contacts':contact
    }
    return render(request,"restaurant.html",context)

def MenuDayIndex(request):
    # total_count = StartersMenu.objects.count()
    # starter = StartersMenu.objects.all()[:total_count-2]
    starter = list(StartersMenu.objects.all())[:-2]
    maincourse = list(MainDishesMenu.objects.all())[:2]
    dessert = DessertsMenu.objects.all()
    drinks = list(DrinkMenu.objects.all())[:3]
    contact = AdminAddress.objects.all()
    context={
        's': starter,
        'm': maincourse,
        'ds': dessert,
        'dr':drinks,
        'contact':contact
    }
    return render(request,"menu-of-the-day.html",context)

def AboutIndex(request):
    contact = AdminAddress.objects.all()
    context={
        'contacts':contact
    }
    return render(request,"about.html",context)

def ContactIndex(request):
    if request.method == 'POST':
        date = request.POST.get('datepicker')
        room_type = request.POST.get('room_type')
        adults = request.POST.get('adults_booking')
        childs = request.POST.get('childs_booking')
        dateTo = request.POST.get('datepickerTo')
        email = request.POST.get('emailId')

        # Check for empty fields if necessary
        if not date or not room_type or not adults or not childs or not dateTo or not email:
            # Handle error: return an error message or render the form again with an error
            return render(request, "index.html", {'error': 'All fields are required.'})

        # Store data in session
        room = Rooms.objects.create(date=date, adultNo=adults, childNo=childs, room=room_type, to_date=dateTo, email=email)
        request.session['room_id'] = room.id
        request.session['room_email'] = room.email

        # Redirect to the same view to avoid re-submission of form data
        return redirect('book_room', id=room.id, email=email)

    room_id = request.session.get('room_id')
    room_email = request.session.get('room_email')

    contact = AdminAddress.objects.all()
    rooms = RoomsType.objects.all()
    context = {
        'rooms': rooms,
        'room_id': room_id,
        'room_email': room_email,
        "contacts":contact
    }
    # for cont in contact:
    #     print(cont.address)  # Print each address in the queryset
    return render(request,"contacts.html",context)

def PlaceIndex(request):
    if request.method == 'POST':
        date = request.POST.get('datepicker')
        room_type = request.POST.get('room_type')
        adults = request.POST.get('adults_booking')
        childs = request.POST.get('childs_booking')
        dateTo = request.POST.get('datepickerTo')
        email = request.POST.get('emailId')

        # Check for empty fields if necessary
        if not date or not room_type or not adults or not childs or not dateTo or not email:
            # Handle error: return an error message or render the form again with an error
            return render(request, "index.html", {'error': 'All fields are required.'})

        # Store data in session
        room = Rooms.objects.create(date=date, adultNo=adults, childNo=childs, room=room_type, to_date=dateTo, email=email)
        request.session['room_id'] = room.id
        request.session['room_email'] = room.email

        # Redirect to the same view to avoid re-submission of form data
        return redirect('book_room', id=room.id, email=email)

    room_id = request.session.get('room_id')
    room_email = request.session.get('room_email')
    places = TouristPlaces.objects.all()
    contact = AdminAddress.objects.all()
    rooms = RoomsType.objects.all()
    paginator = Paginator(places, 6)  # 6 items per page
    page_number = request.GET.get('page')
    try:
        places = paginator.page(page_number)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.page(paginator.num_pages)
    context={
        'places':places,
        'places': places,
        'rooms':rooms,
        'contacts':contact
    }
    return render(request,"famoustouristplaces.html",context)

def PlaceDetails(request,id=None):
    if request.method == 'POST':
        date = request.POST.get('datepicker')
        room_type = request.POST.get('room_type')
        adults = request.POST.get('adults_booking')
        childs = request.POST.get('childs_booking')
        dateTo = request.POST.get('datepickerTo')
        email = request.POST.get('emailId')

        # Check for empty fields if necessary
        if not date or not room_type or not adults or not childs or not dateTo or not email:
            # Handle error: return an error message or render the form again with an error
            return render(request, "index.html", {'error': 'All fields are required.'})

        # Store data in session
        room = Rooms.objects.create(date=date, adultNo=adults, childNo=childs, room=room_type, to_date=dateTo, email=email)
        request.session['room_id'] = room.id
        request.session['room_email'] = room.email

        # Redirect to the same view to avoid re-submission of form data
        return redirect('book_room', id=room.id, email=email)

    room_id = request.session.get('room_id')
    room_email = request.session.get('room_email')
    placeDetails = TouristPlaces.objects.get(id=id)
    contact = AdminAddress.objects.all()
    reachPlace = TourReachPlaces.objects.get(city=placeDetails.city)
    next_place = TouristPlaces.objects.filter(id__gt=id).order_by('id').first()
    previous_place = TouristPlaces.objects.filter(id__lt=id).order_by('-id').first()
    rooms = RoomsType.objects.all()
    context={
        'placeDetails':placeDetails,
        'reachPlace': reachPlace,
        'next_place': next_place,
        'previous_place': previous_place,
        'rooms':rooms,
        'contacts':contact
    }
    return render(request,"place_details.html",context)


########## Email #############
def send_admin_notification_email(context):
    booked_rooms = BookRoom.objects.all()
    room_types = RoomsType.objects.all()
    admin = AdminAddress.objects.first() 
    for booking in booked_rooms:
        context = {
            'user_name': booking.fstname,  # Assuming the user's name is stored in the 'name' field
            'room_name': room_types.get(RoomName=booking.room),
            'booking_date': datetime.now().strftime('%Y-%m-%d'),
            'start_time': booking.date,  # Format time as desired
            'end_time': booking.to_date,  # Format time as desired
            # 'user_view_url': 'https://example.com/user/view-booking',
            'contact_email': 'djangoshivani@gmail.com',
            'company_name': 'PEACE LAND Hotel',
            'email':booking.email,
            'phone':admin.phoneNo  
        }
    subject = 'New Room Booking Request'
    html_message = render_to_string('AdminEmail.html', context)
    plain_message = strip_tags(html_message)  # Strip HTML tags for plain text version
    from_email = 'djangoshivani@gmail.com'
    to_email = ['djangoshivani@gmail.com']  # Add the admin's email address here
    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)


def send_user_confirmation_email(request,book_room, pdf_path):
    booked_rooms = BookRoom.objects.all()
    room_types = RoomsType.objects.all()
    pdf_url = request.build_absolute_uri(settings.MEDIA_URL + os.path.basename(pdf_path))
    print("__________________________",pdf_path)
    for booking in booked_rooms:
        context = {
            'user_name': booking.fstname,  # Assuming the user's name is stored in the 'name' field
            'room_name': room_types.get(RoomName=booking.room),
            'booking_date': datetime.now().strftime('%Y-%m-%d'),
            'start_time': booking.date,  # Format time as desired
            'end_time': booking.to_date, 
            'room_CountNo': booking.room_CountNo,  # Format time as desired
            # 'user_view_url': 'https://example.com/user/view-booking',
            'contact_email': 'djangoshivani@gmail.com',
            'company_name': 'PEACE LAND Hotel',
            'payment_url': 'https://example.com/payment',
            'pdf': pdf_url
        }
    subject = 'Room Booking Confirmation'
    html_message = render_to_string('UserEmail.html', context)
    plain_message = strip_tags(html_message)  # Strip HTML tags for plain text version
    from_email = 'djangoshivani@gmail.com'
    to_email = [booking.email]  # Add the user's email address here

    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)


def generate_booking_pdf(booking, payment_url):
    # Generate QR code
    qr = qrcode.make(payment_url)
    qr_code_path = os.path.join(settings.MEDIA_ROOT, "payment_qr_code.png")
    qr.save(qr_code_path)

    # Create PDF
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Booking Confirmation', 0, 1, 'C')

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        def booking_details(self, booking):
            self.set_font('Arial', '', 12)
            self.cell(0, 10, f"Name: {booking.fstname} {booking.lstname}", 0, 1)
            self.cell(0, 10, f"Email: {booking.email}", 0, 1)
            self.cell(0, 10, f"Phone: {booking.phoneNo}", 0, 1)
            self.cell(0, 10, f"Booking Date: {booking.date}", 0, 1)
            self.cell(0, 10, f"To Date: {booking.to_date}", 0, 1)
            self.cell(0, 10, f"Room: {booking.room.RoomName}", 0, 1)
            room_price = booking.room.RoomPrice
            room_count = booking.room_CountNo
            
            # Debugging: Print values
            print(f"Room Price: {room_price}")
            print(f"Room Count: {room_count}")
            
            # Calculate amount
            amount = int(room_price) * int(room_count)
            self.cell(0, 10, f"Amount: Rs{amount}", 0, 1)

        # def add_qr_code(self, qr_code_path):
        #     self.image(qr_code_path, x=600, y=None, w=30, h=30)
        
        def add_qr_code(self, qr_code_path):
            qr_width, qr_height = 30, 30 # Get the dimensions of the QR code
            pdf_width = self.w - self.r_margin # Get the dimensions of the PDF page
            pdf_height = self.h - self.b_margin
            # Calculate the x and y coordinates to position the QR code at the bottom-right corner
            x = pdf_width - qr_width
            y = pdf_height - qr_height - 100
            self.set_xy(x, y - 10)  # Set position for the text, adjusted 15 units above the QR code
            self.set_font('Arial', '', 10)  # Set font for the text
            self.cell(qr_width, 10, 'Scan and Pay', 0, 1, 'C')  # Add the text centered above the QR code

            self.image(qr_code_path, x=x, y=y, w=qr_width, h=qr_height)  # Add the QR code image


    pdf = PDF()
    pdf.add_page()
    pdf.booking_details(booking)
    pdf.add_qr_code(qr_code_path)

    pdf_output_path = os.path.join(settings.MEDIA_ROOT, f'booking_{booking.fstname}{booking.lstname}.pdf')
    pdf.output(pdf_output_path)
    
    return pdf_output_path



