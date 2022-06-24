TYPE_OF_BUILDING_CHOICES = [
("kamienicy",'kamienicy'),
('bloku', 'bloku'),
('szeregowcu', 'szeregowcu'),
]
NEIGH_FACILITIES_CHOICES = [("BD",'BD')]

NEIGH_SECURITY_CHOICES = [
("ZAMKNIĘTE OSIEDLE",'zamknięte osiedle'),
('OCHRONA', 'ochrona'),
('MONITORING', 'monitoring'),
]

MARKET_CHOICES = [
("WTÓRNY",'wtórny'),
("PIERWOTNY", 'pierwotny'),
]

TYPE_OF_ROOM_CHOICES = [
	("salon",'salon'),
	("salon z aneksem",'salon z aneksem'),
	("pokoj", 'pokój'),
	('korytarz', 'korytarz'),
	('lazienka', 'lazienka'),
	('toaleta', 'wc'),
	('łazienka z wc', 'lazienka z wc'),
	('garderoba', 'garderoba'),
	('pomieszczenie gospodarcze', 'pomieszczenie gospodarcze'),
]

BUILDING_CONDITION_CHOICES = [
("remont dachu",'wyremontowany dach'),
('termomodernizację', 'budynek po termomodernizacji'),
('wymianę instalacji wodno-kanalizacyjnych','instalacja wodno-kanalizacyjna wymieniona'),
]

FLAT_CONDITION_CHOICES = [
	("bardzo dobry",'bardzo dobry'),
	('dobry', 'dobry'),
	('do odświeżenia', 'do odświeżenia'),
	('do remontu', 'do remontu'),
]

PARKING_CHOICES = [
        ('miejsce w garażu podziemnym', 'miejsce w garażu podziemnym'),
        ('miejsce w garażu naziemnym', 'miejsce w garażu naziemnym'),
        ('parking na ulicy', 'parking na ulicy'),
		('nie przynależy', 'nie przynależy')
]

FLAT_ADDITIONAL_SPACES_CHOICES = [
("PIWNICA",'piwnica'),
('SCHOWEK', 'schowek'),
]

WINDOWS_TYPE_CHOICES = [
("PLASTIKOWE",'plastikowe'),
('DREWNIANE', 'drewniane'),
('ALUMINIOWE', 'aluminiowe'),
]

BUILDING_FACILITIES_CHOICES = [
('WINDA','winda'),
('PODJAZD NA WÓZKI', 'podjazd na wózki'),
('WINDA DLA WÓZKÓW', 'winda dla wózków'	),
]

WHY_FLAT_CHANGE_CHOICES = [
	("ZMIANA MIASTA",'zmiany miasta'),
	('ZMIANA NA WIEKSZE', 'zmiany na wieksze'),
	('INNE','inne'),
]

DID_HE_LIVED_CHOICES = [
	('ZAMIESZKIWANE','zamieszkiwane'),
	('WYNAJMOWANE', 'wynajmowane'),
	('INNE', 'inne'),
]

ROOM_ADDITIONAL_SPACE_CHOICES = [
	('brak', 'brak'),
	("z tarasem",'taras'),
	("z wejsciem na ogródek", "ogródek"),
	("z balkonem", "balkon"),
	('z loggia', 'loggia'),
]

WINDOW_IN_ROOM_CHOICES = [
('tak', (
        ('okna na północ', 'na północ'),
   		('okna na wschód', 'na wschód'),
    	('okna na południe', 'na południe'),
   		('okna na zachód', 'na zachód'), 
    	)
    ),
('nie', (
		('bez okien', 'bez okien'),
		)
	),
]

WITH_EQUIPMENT_CHOICES= [
('SOFA','sofa'),
('ZESTAW WYPOCZYNKOWY', 'zestaw wypoczynkowy'),
('KRZESŁA', 'krzesła')
]

WHEN_MOVE_OUT_CHOICES = [
('kilka tygodni', 'za kilka tygodni'),
('około miesiąc', 'za około miesiąc'),
]

OWNERSHIP_RIGHT_CHOICES = [
('własnościowe', 'własnościowe'),
('spółdzielczo-włsnościowe','spółdzielczo-włsnościowe'),
('udział', 'udział'),
]

ATRIBUTE_CHOICES= [
('przestronne', 'przestronne'),
('przytulne','przytulne'),
('funkcjonalne','funkcjonalne'),
('rozkładowe','rozkładowe '),
('słoneczne','sloneczne'),
('zaciszne','zaciszne'),
('dobrze zlokalizowane','dobrze zlokalizowane'), 
('bezpieczne','bezpieczne'),
('duże','duże'),
('nowoczesne','nowoczesne'),
('tradycyjne','tradycyjne'), 
('wyremontowane','wyremontowane'), 
('świetnie skomunikowane','świetnie skomunikowane'), 
('w otoczeniu zieleni','w otoczeniu zieleni'),
('ustawne','ustawne'),
('z pełną infrastrukturą usługowo-handlową','z pełną infrastrukturą usługowo-handlową'),
('wielofunkcyjne ','wielofunkcyjne'),
('prestiżowe ','prestiżowe'),
('wyjątkowe ','wyjątkowe'),
('współczesne ','współczesne'),
('postmodernistyczne ','postmodernistyczne'), 
('rozbudowane ','rozbudowane'),
('rekreacyjne ','rekreacyjne'),
('stylowe','stylowe'),
('niepowtarzalne','niepowtarzalne'), 
('rozwinięte ','rozwinięte'),
('bezpośrednie','bezpośrednie'),
('unikalne','unikalne'),
('niepowtarzalne','niepowtarzalne'), 
('eleganckie','eleganckie'),
('ekskluzywne','ekskluzywne'),
]