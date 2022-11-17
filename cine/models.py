from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PROTECT

'''su = user1
    pass = 071293
    email = user1@gmail.com'''

class User(AbstractUser): # To validated users
    name = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.CharField(max_length=3)
    token = models.CharField(max_length=100, default='', null=True, blank=True)

class Cinema(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=PROTECT)
    name = models.CharField(max_length=20)
    number_seats = models.IntegerField()
    def __str__(self):
        return self.name + ' / ' + self.cinema.name

class Movie(models.Model):
    name = models.CharField(max_length=40)
    duration = models.IntegerField()
    director = models.CharField(max_length=60)
    genre = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Function(models.Model):
    movie = models.ForeignKey(Movie, on_delete=PROTECT)
    room = models.ForeignKey(Room, on_delete=PROTECT)
    date = models.DateField(auto_now_add=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.IntegerField()
    def __str__(self):
        return self.movie.name + ' ' + self.room.name

class Client(models.Model):
    name = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Ticket(models.Model):
    client = models.ForeignKey(Client, on_delete=PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    function = models.ForeignKey(Function, on_delete=PROTECT)
    seats = models.CharField(max_length=50)
    price = models.IntegerField()