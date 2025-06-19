from django.db import models

# Create your models here.

#This table is For Contact details
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
# This table is for room booking function
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    checkin = models.DateField()
    checkout = models.DateField()
    room_type = models.CharField(max_length=100)


# database to book room
class Room_booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    room_type = models.CharField(max_length=50)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.room_type}"

