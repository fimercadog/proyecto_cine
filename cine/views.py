from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from cine.serializer import *


# Create your views here.

class TokenProvider(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user) # To validated token, if token is not created, it must be created
        user.token = token.key
        user.save()
        user_validator = User_serializer(user)
        return Response(user_validator.data)

class Cinema_view(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = Cinema_serializer

class Room_view(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = Room_serializer

class Movie_view(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movie_serializer

class Function_view(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = Function_serializer

class Client_view(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Client_serializer

class Ticket_view(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = Ticket_serializer

class User_view(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serializer


# Show tickets by movie by parameter
class TicketByMovie_view(viewsets.ModelViewSet):
    def get_queryset(self):
        data = self.request.query_params.get('data')
        if data:
            return Ticket.objects.filter(function__movie__name__exact=data)
        else:
            return Ticket.objects.all()
    serializer_class = Ticket_serializer


# Show tickets by clients by age range
class TicketByClientByAgeRange_view(viewsets.ModelViewSet):
    def get_queryset(self):
        data1 = self.request.query_params.get('data1')
        data2 = self.request.query_params.get('data2')
        # TODO insert data on browser ?data1=40&data2=50
        # return Ticket.objects.filter(client__age__gte=data1, client__age__lte=data2)
        if data1 and data2:
            return Ticket.objects.filter(client__age__range=(data1, data2))
        else:
            return Ticket.objects.all()
    serializer_class = Ticket_serializer


# Show tickets by price greater than data
class TicketByPrice_view(viewsets.ModelViewSet):
    def get_queryset(self):
        data = self.request.query_params.get('data')
        if data:
            return Ticket.objects.filter(function__price__gte=data)
        else:
            return Ticket.objects.all()
    serializer_class = Ticket_serializer


# Show tickets by room by seats range
class TicketByRoomBySeatsRange_view(viewsets.ModelViewSet):
    def get_queryset(self):
        data1 = self.request.query_params.get('data1')
        data2 = self.request.query_params.get('data2')
        # return Ticket.objects.filter(function__room__number_seats__gte=data1, function__room__number_seats__lte=data2)
        if data1 and data2:
            return Ticket.objects.filter(function__room__number_seats__range=(data1, data2))
        else:
            return Ticket.objects.all()
    serializer_class = Ticket_serializer


# Show tickets by date of function
class TicketByDateFunction_view(viewsets.ModelViewSet):
    def get_queryset(self):
        data = self.request.query_params.get('data')
        if data:
            return Ticket.objects.filter(function__date__exact=data)
        else:
            return Ticket.objects.all()
    serializer_class = Ticket_serializer


# Show tickets by date range
class TicketByDateRange_view(viewsets.ModelViewSet):
    def get_queryset(self):
        data1 = self.request.query_params.get('data1')
        data2 = self.request.query_params.get('data2')
        # return Ticket.objects.filter(date__gte=data1, date__lte=data2)
        if data1 and data2:
            return Ticket.objects.filter(date__range=(data1, data2))
        else:
            return Ticket.objects.all()
    serializer_class = Ticket_serializer


# Show tickets by legal age clients
class TicketByLegalAge_view(viewsets.ModelViewSet):
    def get_queryset(self):
        data = 18
        return Ticket.objects.filter(client__age__gte=data)

    serializer_class = Ticket_serializer

#* Consultar todas las boletas que se hayan vendido para una pelicula dada por parametro
#* Consultar todas las boletas vendidas para clientes en rango de edades introducidas por parametro
#* 1. obtener todas las boletas que se hayan vendido para una pelicula que se pasan por parametros que
#* 2. obtener todas las boletas que se hayan vendido para salas que tengan mas de x valor pasado por parametro
#* 3. obtener todas las boletas que se hayan vendido para salas que tengan asientos en un rango por parametros
#* 4. Obtener_todas Las boletas que se havan vendida para funciones ofrecidas en una fecha ingresada por parametro
#* 5. Obtener todas las boletas que se havan_vendido_para funciones ofrecidas en_rango de fechas ingresadas por parametro
#* 6. obtener todas las boletas que se hayan para clientes mayores de edad