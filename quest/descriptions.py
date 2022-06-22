from .models import Quest


def get_example_desc():
	quest_id = Quest.objects.latest('id').id
	quest = Quest.objects.get(id = quest_id)
	"""
		name_of_city
		name_of_street
		market 	
		floor_area
		how_many_rooms
		how_many_levels
		price 
		which_flor 
		how_many_flors
		flat_condition 
		how_high
		flat_facilities 
		why_flat_change
		type_of_building
		around_facilities 
		around_security 
		building_condition 
		
		atribute2
		how_many_rooms
		name_of_street
		"""

	EXAMPLE_DESCRIPTION = [
	(f' <strong> {quest.how_many_rooms}-pokojowe mieszkanie przy ul. {quest.name_of_street} szuka nowego właściciela! </strong> <br>\
	<br>\
	<strong> W skrócie...</strong> <br>\
	Z bólem serca, z powodu <why_flat_change>, szukam nowego włąściciela do mojego <atribute1>, M<how_many_rooms>, zlokalizowanego na ulicy <name_of_street> na Saskiej Kępie. \
	Mieszkanie jest <atribute2> i <atribute3>, \
	<czy_sprzedaje_z_wyposażeniem> i <czy_umeblowane> w pełni umeblowane i gotowe do zamieszkania od ręki. \
	Stacja metra Centrum Nauki Kopernik ok. 4 minuty spacerem! \
	Jeżeli tego właśnie szukasz, zapraszam po więcej szczegółów poniżej. <br>\
	<br>\
	<strong> Mieszkanie </strong> <br>\
	Na powierzchnię <floor_area> skłąda się:\
	<room_1> - <floor_area>\
	W ostatnich latach dokonano wymiany instalacji elektrycznej i cieplnej, dzięki czemu jest ono bezpieczne w codziennym użytkowaniu.\
	Okna są nowe, wykonane z plastiku. Czynsz dla 4 osób wynosi 600 zł. <br>\
	<br>\
	<strong> Budynek </strong> <br>\
	Nieruchomość znajduje się w <type_of_building> z <year_of_building> roku. W ostatnich latach przeprowadzono remont klatek schodowych i balkonów, a cały blok jest po termomodernizacji. W <type_of_building> znajduje się <building_facilities>. \
	Wspólnota mieszkaniowa dba o budynek, a części wspólne są czyste i schludne. \
	Tereny wokół bloku są również zadbane. Do mieszkania przynależy również naziemne miejsce parkingowe. \
	Budynek wyposażony jest w podjazd dla niepełnosprawnych.<br>\
	<br>\
	<strong> Lokalizacja </strong><br>\
	W bezpośrednim sąsiedztwie znajduje się boisko piłkarskie, a także wiele parków oraz plac zabaw. \
	Nieopodal zlokalizowane są również szkoły podstawowe oraz publiczne przedszkola. \
	W odległości 2 km od nieruchomości mieści się natomiast uniwersytet medyczny. \
	Dzięki bliskiej lokalizacji sklepów spożywczych, drogerii i aptek można szybko i bezproblemowo\
	zakupić żywność i produkty codziennego użytku. Okolica cieszy się najwyższym w mieście wskaźnikiem jakości powietrza.  <br>\
	<br>\
	<strong> Komunikacja i okolica </strong> <br>\
	Okolica jest dobrze skomunikowana, bowiem ze znajdującego się w odległości 300 metrów od budynku przystanku autobusowego można bezpośrednio dojechać zarówno do centrum, jak i na lotnisko. Ponadto 200 metrów od budynku znajduje się przystanek szybkiej kolei miejskiej. Najbliższy przystanek tramwajowy mieście się w odległości 500 metrów od bloku. Spacer do opisanych wyżej punktów komunikacji miejskiej zajmuje około 5 minut.<br>'
	)
	]



