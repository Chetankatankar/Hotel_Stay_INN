# from django.shortcuts import render
from .models import Contact

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Booking  # create this model if not created
from django.contrib import messages

from .models import Room_booking


# Create your views here.

# Contact details savingg process
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Save to database logic here


        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('contact')
    
    return render(request, 'contact.html')
    

# routes
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def rooms(request):
    return render(request, 'rooms.html')

def room_book(request):
    return render(request, 'book_room.html')

# function for room booking 
@csrf_exempt
def book_room(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        room_type = request.POST.get('room_type')

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            checkin=checkin,
            checkout=checkout,
            room_type=room_type
        )

        messages.success(request, "Thank you for your bookingg!😊")
    return redirect('home')


# Another room booking form 
def room_book(request):
    if request.method == 'POST':
        Room_booking.objects.create(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            room_type=request.POST['room_type'],
            check_in=request.POST['check_in'],
            check_out=request.POST['check_out'],
            guests=request.POST['guests'],
            special_requests=request.POST.get('special_requests', '')
        )
        return render(request, 'thankyou.html')  # After booking
    return render(request, 'book_room.html')
