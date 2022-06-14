TYPE_OF_BUILDING_CHOICES = [("BD",'BD')]
AROUND_FACILITIES_CHOICES = [("BD",'BD')]
AROUND_SECURITY_CHOICES = [("BD",'BD')]
BUILDING_MATERIAL_CHOICES = [("BD",'BD')]
NAIGHBOURHOOD_CHOICES = [("BD",'BD')]
LOCALIZATION_CHOICES = [("BD",'BD')]
MARKET_CHOICES = [("BD",'BD')]

TYPE_OF_SPACE_CHOICES = [
	("SALON",'salon'),
	("POKOJ", 'pokoj'),
	('KORYTARZ', 'korytarz'),
	('LAZIENKA', 'lazienka'),
	('TOALETA', 'wc'),
	('ŁAZIENKA Z WC', 'lazienka z wc'),
	('GARDEROBA', 'garderoba'),
	('POMIESZCZENIE GOSPODARCZE', 'pomieszczenie gospodarcze'),
]

TECHNICAL_CONDITION_CHOICES = [
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

FLAT_ADDITIONAL_SPACES_CHOICES = [
("PIWNICA",'piwnica'),
('SCHOWEK', 'schowek'),
('MIEJSCE PARKINGOWE', (
        ('PODZIEMNE', 'miejsce w garażu podziemnym'),
        ('GARAZ', 'miejsce w garażu naziemnym'),
        ('NA_ULICY', 'parking na ulicy'),
    	)
    ),
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

SPACE_ADDITIONAL_SPACE_CHOICES = [
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
