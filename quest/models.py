from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

from .constants import *


class Quest(models.Model):
	#Flat
	name_of_city = models.CharField(max_length=50, verbose_name='Miasto')
	name_of_street = models.CharField(max_length=30, verbose_name='Nazwa ulicy')
	market = models.CharField(max_length=30, verbose_name='Rynek',choices=MARKET_CHOICES, null=True)
	atribute1 = models.CharField(max_length=130, verbose_name='Cecha 1', choices=ATRIBUTE_CHOICES, null=True)
	atribute2 = models.CharField(max_length=130, verbose_name='Cecha 2', choices=ATRIBUTE_CHOICES, null=True)
	atribute3 = models.CharField(max_length=130, verbose_name='Cecha 3', choices=ATRIBUTE_CHOICES, null=True)
	why_flat_change = MultiSelectField(max_length=30, verbose_name='Sprzedaje z powodu', choices=WHY_FLAT_CHANGE_CHOICES, null=True)	
	with_equimpent = MultiSelectField(max_length=300, verbose_name='Wyposażenie wnętrz', choices=WITH_EQUIPMENT_CHOICES, null=True)
	when_move_out = models.CharField(max_length=30, verbose_name='Wolne od', choices=WHEN_MOVE_OUT_CHOICES, null=True)
	flat_additional_spaces = MultiSelectField(max_length=30, verbose_name='Pomieszczenia dodatkowe', choices=FLAT_ADDITIONAL_SPACES_CHOICES)
	#ownership_right = MultiSelectField(max_length=30, choices=OWNERSHIP_RIGHT_CHOICES)
	how_many_people = models.PositiveIntegerField(verbose_name='Ile osób zamieszkiwało',
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	flat_utilities = models.IntegerField('Czynsz administracyjny', help_text='PLN/msc',
		validators=[
			MaxValueValidator(2000),
			MinValueValidator(0)
		]
	)
	number_of_building = models.PositiveIntegerField(verbose_name='Numer budynku',
		validators=[
			MaxValueValidator(300),
			MinValueValidator(1),
		]
	)
	floor_area = models.PositiveIntegerField(verbose_name='Powierzchnia (m2)',
		validators=[
			MaxValueValidator(250),
			MinValueValidator(1),
		]
	)
	how_many_rooms= models.PositiveIntegerField(verbose_name='Liczba pokoi',
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	price = models.PositiveIntegerField(verbose_name='Cena', help_text='PLN',
		validators=[
			MaxValueValidator(20000000),
			MinValueValidator(1)
		]
	)
	which_floor = models.PositiveIntegerField(verbose_name='Kondygnacja',
		validators=[
			MaxValueValidator(60),
			MinValueValidator(0)
		]
	)
	how_many_floors = models.PositiveIntegerField(verbose_name='Pięter w budynku',
		validators=[
			MaxValueValidator(60),
			MinValueValidator(1)
		]
	)
	flat_condition = models.CharField(max_length=30, verbose_name='Stan mieszkania', choices=FLAT_CONDITION_CHOICES, null=True)
	how_high = models.PositiveIntegerField(verbose_name='Wysokość pomieszczeń', help_text='cm',
		validators=[
			MaxValueValidator(500),
			MinValueValidator(1)
		]
	)
	#Building
	type_of_building = models.CharField(max_length=30, verbose_name='Rodzaj budynku', choices=TYPE_OF_BUILDING_CHOICES, null=True)
	#building_material = models.CharField(max_length=30, choices=BUILDING_MATERIAL_CHOICES)
	neigh_security = MultiSelectField(max_length=300, verbose_name='Bezpieczeństwo okolicy', choices=NEIGH_SECURITY_CHOICES, null=True)
	building_condition = MultiSelectField(max_length=300, verbose_name='Prace przeprowadzone w budynku', choices=BUILDING_CONDITION_CHOICES, null=True)
	parking = models.CharField(max_length=30, verbose_name='Parking', choices=PARKING_CHOICES, null=True)
	building_facitilities = MultiSelectField(max_length=300, verbose_name='Udogodnienia w budynku i okolicy', choices=BUILDING_FACILITIES_CHOICES, null=True)
	#neighborghood = models.CharField(max_length=30, choices=NAIGHBOURHOOD_CHOICES)
	year_of_building = models.IntegerField(verbose_name='Rok budowy',
			validators=[
				MaxValueValidator(2023),
				MinValueValidator(1000)
			]
		)
	

class Room(models.Model):
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='rooms')
	floor_area = models.PositiveIntegerField(verbose_name='metraż')
	type_of_room = models.CharField(max_length=70, verbose_name='Rodzaj pomieszczenia', choices=TYPE_OF_ROOM_CHOICES, null=True)
	room_additional_space = models.CharField(max_length=70, verbose_name='Powierzchnie przynależne', choices=ROOM_ADDITIONAL_SPACE_CHOICES, null=True)
	window_in_room = models.CharField(max_length=70, verbose_name='Ekspozycja okien', choices=WINDOW_IN_ROOM_CHOICES, null=True)
