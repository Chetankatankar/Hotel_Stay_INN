from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('rooms', views.rooms, name='rooms'),
    path('book-room/', views.book_room, name='book_room'),  #book room form url
    path('contact-form/', views.contact_view, name='contact'),   #Conatct form url
    path('room_book/', views.room_book, name='room_book'),

]