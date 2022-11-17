from rest_framework import serializers
from cine.models import *


class Cinema_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class Room_serializer(serializers.ModelSerializer):
    cinema = Cinema_serializer(read_only=True)
    cinema_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cinema.objects.all(), source='cinema')
    class Meta:
        model = Room
        fields = '__all__'

class Movie_serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class Function_serializer(serializers.ModelSerializer):
    movie = Movie_serializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Movie.objects.all(), source='movie')
    room = Room_serializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Room.objects.all(), source='room')
    class Meta:
        model = Function
        fields = '__all__'

class Client_serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class Ticket_serializer(serializers.ModelSerializer):
    client = Client_serializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Client.objects.all(), source='client')
    function = Function_serializer(read_only=True)
    function_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Function.objects.all(), source='function')
    class Meta:
        model = Ticket
        fields = '__all__'

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            name = validated_data['name'],
            telephone = validated_data['telephone'],
            email = validated_data['email'],
            age = validated_data['age'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user