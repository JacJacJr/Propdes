TYPE_OF_BUILDING_CHOICES = [("BD",'BD')]
AROUND_FACILITIES_CHOICES = [("BD",'BD')]
AROUND_SECURITY_CHOICES = [("BD",'BD')]
BUILDING_MATERIAL_CHOICES = [("BD",'BD')]
NAIGHBOURHOOD_CHOICES = [("BD",'BD')]
LOCALIZATION_CHOICES = [("BD",'BD')]


MARKET_CHOICES = [
("WTÓRNY",'wtórny'),
("PIERWOTNY", 'pierwotny'),
]

TYPE_OF_ROOM_CHOICES = [
	("SALON",'salon'),
	("SALON Z ANEKSEM",'salon z aneksem'),
	("POKOJ", 'pokoj'),
	('KORYTARZ', 'korytarz'),
	('LAZIENKA', 'lazienka'),
	('TOALETA', 'wc'),
	('ŁAZIENKA Z WC', 'lazienka z wc'),
	('GARDEROBA', 'garderoba'),
	('POMIESZCZENIE GOSPODARCZE', 'pomieszczenie gospodarcze'),
]

BUILDING_CONDITION_CHOICES = [("BD",'BD')]

FLAT_CONDITION_CHOICES = [
	("PO_REMONCIE",'po remoncie'),
	('DOBRY', 'dobry'),
	('DO_REMONTU', 'do remontu'),
]

TYPE_OF_KITCHEN_CHOICES = [
('ODDZIELNA', 'oddzielna'),
('ANEKS KUCHENNY', 'aneks kuchenny'),
]

TYPE_OF_HEATING_CHOICES = [
("MIEJSKIE",'miejskie'),
('GAZOWE', 'gazowe'),
('ELEKTRYCZNE', 'elektryczne'),
('KOTŁOWNIA', 'kotłownia'),
]

PARKING_CHOICES = [
('MIEJSCE PARKINGOWE', (
        ('PODZIEMNE', 'miejsce w garażu podziemnym'),
        ('GARAZ', 'miejsce w garażu naziemnym'),
        ('NA_ULICY', 'parking na ulicy'),
    	)
    ),
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

FACILITIES_CHOICES = [
('WINDA','winda'),
('PODJAZD NA WÓZKI', 'podjazd na wózki'),
('WINDA DLA WÓZKÓW', 'winda dla wózków'	),
]

WHY_FLAT_CHANGE_CHOICES = [
	("ZMIANA MIASTA",'zmiana miasta'),
	('ZMIANA NA WIĘKSZE', 'zmiana na większe'),
	('INNE','inne'),
]

DID_HE_LIVED_CHOICES = [
	('ZAMIESZKIWANE','zamieszkiwane'),
	('WYNAJMOWANE', 'wynajmowane'),
	('INNE', 'inne'),
]

ROOM_ADDITIONAL_SPACE_CHOICES = [
	("TARAS",'taras'),
	("OGRÓDEK", "ogródek"),
	("BALKON LOGIA", "balkon loggia"),
]

WINDOW_IN_SPACE_CHOICES = [
    ('TAK', (
            ('PŁ', 'na północ'),
            ('WSCH', 'na wschód'),
            ('PŁD', 'na południe'),
            ('ZACH', 'na zachód'),
        )
    ),
    ('NIE', (
    		#czy to można pominąć?
            ('NIE', 'NIE'),
        )
    ),
]

ATRIBUTE_CHOICES= [
('PRZESTRONNE', 'przestronne'),
('PRZYTULNE','przytulne'),
('FUNKCJONALNE','funkcjonalne'),
('ROZKŁADOWE','rozkładowe '),
('SŁONECZNE','sloneczne'),
('ZACISZNE','zaciszne'),
('DOBRZE ZLOKALIZOWANE','dobrze zlokalizowane'), 
('BEZPIECZNE','bezpieczne'),
('DUŻE','duże'),
('NOWOCZESNE','nowoczesne'),
('TRADYCYJNE','tradycyjne'), 
('WYREMONTOWANE','wyremontowane'), 
('ŚWIETNIE SKOMUNIKOWANE','świetnie skomunikowane'), 
('W OTOCZENIU ZIELENI','w otoczeniu zieleni'),
('USTAWNE','ustawne'),
('Z PEŁNĄ INFRASTRUKTURĄ USŁUGOWO-HANDLOWĄ','z pełną infrastrukturą usługowo-handlową'),
('WIELOFUNKCYJNE ','wielofunkcyjne'),
('PRESTIŻOWE ','prestiżowe'),
('WYJĄTKOWE ','wyjątkowe'),
('WSPÓŁCZESNE ','współczesne'),
('POSTMODERNISTYCZNE ','postmodernistyczne'), 
('ROZBUDOWANE ','rozbudowane'),
('REKREACYJNE ','rekreacyjne'),
('STYLOWE','stylowe'),
('NIEPOWTARZALNE','niepowtarzalne'), 
('ROZWINIĘTE ','rozwinięte'),
('BEZPOŚREDNIE','bezpośrednie'),
('UNIKALNE','unikalne'),
('NIEPOWTARZALNE','niepowtarzalne'), 
('ELEGANCKIE','eleganckie'),
('EKSKLUZYWNE','ekskluzywne'),
]
