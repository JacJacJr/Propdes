from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .constants import *

class Quest(models.Model):
	#Flat
	name_of_city = models.CharField(max_length=30, help_text='Miasto')
	name_of_street = models.CharField(max_length=30, help_text='Ulica')
	market = models.CharField(max_length=30, help_text='Rynek',choices=MARKET_CHOICES)
	floor_area = models.IntegerField(help_text='m2',
		validators=[
			MaxValueValidator(300),
			MinValueValidator(1),
		]
	)
	how_many_rooms= models.IntegerField(help_text='Ilość pokoi',
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	how_many_levels= models.IntegerField(help_text='Ile pięter w mieszkaniu?',
			validators=[
				MaxValueValidator(3),
				MinValueValidator(1)
		]
	)
	price = models.IntegerField(help_text='Cena',
		validators=[
			MaxValueValidator(20000000),
			MinValueValidator(1)
		]
	)
	which_flor = models.IntegerField(help_text='Piętro w budynku',
		validators=[
			MaxValueValidator(60),
			MinValueValidator(1)
		]
	)
	how_many_flors = models.IntegerField(help_text='Ile pięter w budynku?',
		validators=[
			MaxValueValidator(60),
			MinValueValidator(1)
		]
	)
	flat_condition = models.CharField(max_length=30, help_text='Stan mieszkania', choices=FLAT_CONDITION_CHOICES)
	how_high = models.IntegerField(help_text='Wysokość w cm',
		validators=[
			MaxValueValidator(500),
			MinValueValidator(1)
		]
	)
	#jak zrobić żeby tu był wielokrotny wybór?!
	flat_facilities = models.CharField(max_length=30, help_text='Udogodnienia', choices=FACILITIES_CHOICES)
	why_flat_change = models.CharField(max_length=30, help_text='Powód zmiany nieruchomości', choices=WHY_FLAT_CHANGE_CHOICES)
	"""
	#Rooms
	#czy aneks kuchenny będzie typem pokoju? raczej byłby chackboxem do zaznaczenia
	type_of_space = models.CharField(max_length=30, choices=TYPE_OF_SPACE_CHOICES)
	#space_additional_space = models.CharField(max_lenght=30, choices= SPACE_ADDITIONAL_SPACE_CHOICES)
	#window_in_space = models.CharField(max_lenght=20, choices=WINDOW_IN_SPACE_CHOICES)
	floor_area= models.IntegerField(
		validators=[
			MaxValueValidator(100),
			MinValueValidator(1),
		]
	)
	"""
	#Building
	type_of_building = models.CharField(max_length=30, help_text='Rodzaj budynku', choices=TYPE_OF_BUILDING_CHOICES)
	around_facilities = models.CharField(max_length=30, help_text='Udogodnienia w budynku', choices=AROUND_FACILITIES_CHOICES)
	around_security = models.CharField(max_length=30, help_text='Bezpieczeństwo okolicy', choices=AROUND_SECURITY_CHOICES)
	building_condition = models.CharField(max_length=30, help_text='Stan budynku', choices=BUILDING_CONDITION_CHOICES)
	#Localization
	#Z_formularzy
	#Transport
	#Z_formularzy

#To mi się już chyba raczej nie przyda....
"""
class Flat(models.Model):
	name_of_city = models.CharField(max_length=50)
	name_of_street = models.CharField(max_length=50)
	market = models.CharField(max_length=30, choices=MARKET_CHOICES)
	ownership_right = models.CharField(max_length=30, choices=TYPE_OF_SPACE_CHOICES)
	flat_condition = models.CharField(max_length=30, choices=FLAT_CONDITION_CHOICES)
	type_of_kitchen = models.CharField(max_length=30, choices=TYPE_OF_KITCHEN_CHOICES)
	type_of_heating = models.CharField(max_length=30, choices=TYPE_OF_HEATING_CHOICES)
	#nie koniecznie będzie jedna
	flat_additional_spaces = models.CharField(max_length=30, choices=FLAT_ADDITIONAL_SPACES_CHOICES)
	windows_type = models.CharField(max_length=30, choices=WINDOWS_TYPE_CHOICES)
	flat_facilities = models.CharField(max_length=30, choices=FACILITIES_CHOICES)
	why_flat_change = models.CharField(max_length=30, choices=WHY_FLAT_CHANGE_CHOICES)
	did_he_lived = models.CharField(max_length=30, choices=DID_HE_LIVED_CHOICES)
	bathroom_wc_together = models.CharField(max_length=30, choices=[('YES', 'tak'),('NO', 'nie'),])
	#jak wyświetlać jednostki
	floor_area = models.IntegerField(help_text='m2',
		validators=[
			MaxValueValidator(300),
			MinValueValidator(1),
		]
	)

	how_many_rooms= models.IntegerField(
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	how_many_levels= models.IntegerField(
			validators=[
				MaxValueValidator(3),
				MinValueValidator(1)
		]
	)
	price = models.IntegerField(
		validators=[
			MaxValueValidator(20000000),
			MinValueValidator(1)
		]
	)
	which_flor = models.IntegerField(
		validators=[
			MaxValueValidator(60),
			MinValueValidator(1)
		]
	)
	how_many_flors = models.IntegerField(
		validators=[
			MaxValueValidator(60),
			MinValueValidator(1)
		]
	)
	how_high = models.IntegerField(
		validators=[
			MaxValueValidator(500),
			MinValueValidator(1)
		]
	)
	amount_of_fees = models.IntegerField(
		validators=[
			MaxValueValidator(1500),
			MinValueValidator(1)
		]
	)
	how_many_tenants = models.IntegerField(
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	flat_utilities = models.IntegerField(
		validators=[
			MaxValueValidator(1000),
			MinValueValidator(0)
		]
	)

class Space(models.Model):
	flat_id= models.ForeignKey(Flat, on_delete=models.CASCADE)
	#czy aneks kuchenny będzie typem pokoju? raczej byłby chackboxem do zaznaczenia
	type_of_space = models.CharField(max_length=30, choices=TYPE_OF_SPACE_CHOICES)
	#space_additional_space = models.CharField(max_lenght=30, choices= SPACE_ADDITIONAL_SPACE_CHOICES)
	#window_in_space = models.CharField(max_lenght=20, choices=WINDOW_IN_SPACE_CHOICES)
	floor_area= models.IntegerField(
		validators=[
			MaxValueValidator(100),
			MinValueValidator(1),
		]
	)

class Around(models.Model):
	flat_id= models.ForeignKey(Flat, on_delete=models.CASCADE)
	type_of_building = models.CharField(max_length=30, choices=TYPE_OF_BUILDING_CHOICES)
	around_facilities = models.CharField(max_length=30, choices=AROUND_FACILITIES_CHOICES)
	around_security = models.CharField(max_length=30, choices=AROUND_SECURITY_CHOICES)
	building_material = models.CharField(max_length=30, choices=BUILDING_MATERIAL_CHOICES)
	neighborghood = models.CharField(max_length=30, choices=NAIGHBOURHOOD_CHOICES)
	localization = models.CharField(max_length=30, choices=LOCALIZATION_CHOICES)
	year_of_building = models.IntegerField(
		validators=[
			MaxValueValidator(2023),
			MinValueValidator(1000)
		]
	)
#próbuję z tym. może lepiej stworzyć jedną klasę która pobiera dane...


	 NA PRZYSZŁOŚĆ !!!
	chcę, aby na widoku w którym klient deklaruje ilośc pokoi, 
	#pokazywało się najpierw pole pokoi, oraz przycisk(dodaj pomieszczenie) 
	kótre po kliknięciu stworzy następne. Ich ilość będzie tutaj wpisana - 
	ALE CZY JEST TO POTRZEBNE?
	#na pewno będzie potrzebne tutaj numer tego pomieszczenia!
	number_of_spaces = models.IntegerField(
		validators=[
			MaxValueValidator(100),
			MinValueValidator(1)
		]
	)
	#to będziemy łączyć z przejściami do innych pokoi - czy mi się to przyda?!
	conented_with = models.CharField(max_length=10, choices=type_of_rooms_CHOICES)
	
	KONIEC
"""