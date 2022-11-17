from rest_framework import routers
from django.urls import path, include
from cine.views import *


router = routers.DefaultRouter()
router.register('cinema', Cinema_view, basename='cinema')
router.register('room', Room_view, basename='room')
router.register('movie', Movie_view, basename='movie')
router.register('function', Function_view, basename='function')
router.register('client', Client_view, basename='client')
router.register('ticket', Ticket_view, basename='ticket')
router.register('user', User_view, basename='user')
router.register('ticketbymovie', TicketByMovie_view, basename='ticketbymovie')
router.register('ticketbyprice', TicketByPrice_view, basename='ticketbyprice')
router.register('ticketbydatefunction', TicketByDateFunction_view, basename='ticketbydatefunction')
router.register('ticketbylegalage', TicketByLegalAge_view, basename='ticketbylegalage')
router.register('ticketbyagerange', TicketByClientByAgeRange_view, basename='ticketbyagerange')
router.register('ticketbydaterange', TicketByDateRange_view, basename='ticketbydaterange')


urlpatterns = [
    path('', include(router.urls)),
    path('token',TokenProvider.as_view(), name = 'token'),
]
