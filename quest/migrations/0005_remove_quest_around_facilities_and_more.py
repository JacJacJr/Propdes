# Generated by Django 4.0.5 on 2022-06-23 16:39

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0004_remove_quest_how_many_levels_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='around_facilities',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='around_security',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='flat_facilities',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='type_of_room',
        ),
        migrations.RemoveField(
            model_name='room',
            name='metrage',
        ),
        migrations.AddField(
            model_name='quest',
            name='atribute1',
            field=models.CharField(choices=[('PRZESTRONNE', 'przestronne'), ('PRZYTULNE', 'przytulne'), ('FUNKCJONALNE', 'funkcjonalne'), ('ROZKŁADOWE', 'rozkładowe '), ('SŁONECZNE', 'sloneczne'), ('ZACISZNE', 'zaciszne'), ('DOBRZE ZLOKALIZOWANE', 'dobrze zlokalizowane'), ('BEZPIECZNE', 'bezpieczne'), ('DUŻE', 'duże'), ('NOWOCZESNE', 'nowoczesne'), ('TRADYCYJNE', 'tradycyjne'), ('WYREMONTOWANE', 'wyremontowane'), ('ŚWIETNIE SKOMUNIKOWANE', 'świetnie skomunikowane'), ('W OTOCZENIU ZIELENI', 'w otoczeniu zieleni'), ('USTAWNE', 'ustawne'), ('Z PEŁNĄ INFRASTRUKTURĄ USŁUGOWO-HANDLOWĄ', 'z pełną infrastrukturą usługowo-handlową'), ('WIELOFUNKCYJNE ', 'wielofunkcyjne'), ('PRESTIŻOWE ', 'prestiżowe'), ('WYJĄTKOWE ', 'wyjątkowe'), ('WSPÓŁCZESNE ', 'współczesne'), ('POSTMODERNISTYCZNE ', 'postmodernistyczne'), ('ROZBUDOWANE ', 'rozbudowane'), ('REKREACYJNE ', 'rekreacyjne'), ('STYLOWE', 'stylowe'), ('NIEPOWTARZALNE', 'niepowtarzalne'), ('ROZWINIĘTE ', 'rozwinięte'), ('BEZPOŚREDNIE', 'bezpośrednie'), ('UNIKALNE', 'unikalne'), ('NIEPOWTARZALNE', 'niepowtarzalne'), ('ELEGANCKIE', 'eleganckie'), ('EKSKLUZYWNE', 'ekskluzywne')], max_length=130, null=True, verbose_name='Cecha 1'),
        ),
        migrations.AddField(
            model_name='quest',
            name='atribute2',
            field=models.CharField(choices=[('PRZESTRONNE', 'przestronne'), ('PRZYTULNE', 'przytulne'), ('FUNKCJONALNE', 'funkcjonalne'), ('ROZKŁADOWE', 'rozkładowe '), ('SŁONECZNE', 'sloneczne'), ('ZACISZNE', 'zaciszne'), ('DOBRZE ZLOKALIZOWANE', 'dobrze zlokalizowane'), ('BEZPIECZNE', 'bezpieczne'), ('DUŻE', 'duże'), ('NOWOCZESNE', 'nowoczesne'), ('TRADYCYJNE', 'tradycyjne'), ('WYREMONTOWANE', 'wyremontowane'), ('ŚWIETNIE SKOMUNIKOWANE', 'świetnie skomunikowane'), ('W OTOCZENIU ZIELENI', 'w otoczeniu zieleni'), ('USTAWNE', 'ustawne'), ('Z PEŁNĄ INFRASTRUKTURĄ USŁUGOWO-HANDLOWĄ', 'z pełną infrastrukturą usługowo-handlową'), ('WIELOFUNKCYJNE ', 'wielofunkcyjne'), ('PRESTIŻOWE ', 'prestiżowe'), ('WYJĄTKOWE ', 'wyjątkowe'), ('WSPÓŁCZESNE ', 'współczesne'), ('POSTMODERNISTYCZNE ', 'postmodernistyczne'), ('ROZBUDOWANE ', 'rozbudowane'), ('REKREACYJNE ', 'rekreacyjne'), ('STYLOWE', 'stylowe'), ('NIEPOWTARZALNE', 'niepowtarzalne'), ('ROZWINIĘTE ', 'rozwinięte'), ('BEZPOŚREDNIE', 'bezpośrednie'), ('UNIKALNE', 'unikalne'), ('NIEPOWTARZALNE', 'niepowtarzalne'), ('ELEGANCKIE', 'eleganckie'), ('EKSKLUZYWNE', 'ekskluzywne')], max_length=130, null=True, verbose_name='Cecha 2'),
        ),
        migrations.AddField(
            model_name='quest',
            name='atribute3',
            field=models.CharField(choices=[('PRZESTRONNE', 'przestronne'), ('PRZYTULNE', 'przytulne'), ('FUNKCJONALNE', 'funkcjonalne'), ('ROZKŁADOWE', 'rozkładowe '), ('SŁONECZNE', 'sloneczne'), ('ZACISZNE', 'zaciszne'), ('DOBRZE ZLOKALIZOWANE', 'dobrze zlokalizowane'), ('BEZPIECZNE', 'bezpieczne'), ('DUŻE', 'duże'), ('NOWOCZESNE', 'nowoczesne'), ('TRADYCYJNE', 'tradycyjne'), ('WYREMONTOWANE', 'wyremontowane'), ('ŚWIETNIE SKOMUNIKOWANE', 'świetnie skomunikowane'), ('W OTOCZENIU ZIELENI', 'w otoczeniu zieleni'), ('USTAWNE', 'ustawne'), ('Z PEŁNĄ INFRASTRUKTURĄ USŁUGOWO-HANDLOWĄ', 'z pełną infrastrukturą usługowo-handlową'), ('WIELOFUNKCYJNE ', 'wielofunkcyjne'), ('PRESTIŻOWE ', 'prestiżowe'), ('WYJĄTKOWE ', 'wyjątkowe'), ('WSPÓŁCZESNE ', 'współczesne'), ('POSTMODERNISTYCZNE ', 'postmodernistyczne'), ('ROZBUDOWANE ', 'rozbudowane'), ('REKREACYJNE ', 'rekreacyjne'), ('STYLOWE', 'stylowe'), ('NIEPOWTARZALNE', 'niepowtarzalne'), ('ROZWINIĘTE ', 'rozwinięte'), ('BEZPOŚREDNIE', 'bezpośrednie'), ('UNIKALNE', 'unikalne'), ('NIEPOWTARZALNE', 'niepowtarzalne'), ('ELEGANCKIE', 'eleganckie'), ('EKSKLUZYWNE', 'ekskluzywne')], max_length=130, null=True, verbose_name='Cecha 3'),
        ),
        migrations.AddField(
            model_name='quest',
            name='building_facitilities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('WINDA', 'winda'), ('PODJAZD NA WÓZKI', 'podjazd na wózki'), ('WINDA DLA WÓZKÓW', 'winda dla wózków')], max_length=300, null=True, verbose_name='Udogodnienia w budynku i okolicy'),
        ),
        migrations.AddField(
            model_name='quest',
            name='flat_additional_spaces',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('PIWNICA', 'piwnica'), ('SCHOWEK', 'schowek')], default=1, max_length=30, verbose_name='Pomieszczenia dodatkowe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='flat_utilities',
            field=models.IntegerField(default=1, help_text='PLN/msc', validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(0)], verbose_name='Czynsz administracyjny'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='how_many_people',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Ile osób zamieszkiwało'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='neigh_security',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ZAMKNIĘTE OSIEDLE', 'zamknięte osiedle'), ('OCHRONA', 'ochrona'), ('MONITORING', 'monitoring')], max_length=300, null=True, verbose_name='Bezpieczeństwo okolicy'),
        ),
        migrations.AddField(
            model_name='quest',
            name='parking',
            field=models.CharField(choices=[('PODZIEMNE', 'miejsce w garażu podziemnym'), ('GARAZ', 'miejsce w garażu naziemnym'), ('NA_ULICY', 'parking na ulicy'), ('NIE PRZYNALEŻY', 'nie przynależy')], max_length=30, null=True, verbose_name='Parking'),
        ),
        migrations.AddField(
            model_name='quest',
            name='when_move_out',
            field=models.CharField(choices=[('OD RĘKI', 'od ręki'), ('KILKA TYGODNI', 'za kilka tygodni'), ('OKOŁO MIESIĄC', 'za około miesiąc')], max_length=30, null=True, verbose_name='Wolne od'),
        ),
        migrations.AddField(
            model_name='quest',
            name='with_equimpent',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('SOFA', 'sofa'), ('ZESTAW WYPOCZYNKOWY', 'zestaw wypoczynkowy'), ('KRZESŁA', 'krzesła')], max_length=300, null=True, verbose_name='Wyposażenie wnętrz'),
        ),
        migrations.AddField(
            model_name='quest',
            name='year_of_building',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1000)], verbose_name='Rok budowy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='floor_area',
            field=models.PositiveIntegerField(default=1, help_text='m2', verbose_name='metraż'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_additional_space',
            field=models.CharField(choices=[('brak', 'brak'), ('TARAS', 'taras'), ('OGRÓDEK', 'ogródek'), ('BALKON LOGIA', 'balkon loggia')], max_length=70, null=True, verbose_name='Powierzchnie przynależne'),
        ),
        migrations.AddField(
            model_name='room',
            name='type_of_room',
            field=models.CharField(choices=[('SALON', 'salon'), ('SALON Z ANEKSEM', 'salon z aneksem'), ('POKOJ', 'pokój'), ('KORYTARZ', 'korytarz'), ('LAZIENKA', 'lazienka'), ('TOALETA', 'wc'), ('ŁAZIENKA Z WC', 'lazienka z wc'), ('GARDEROBA', 'garderoba'), ('POMIESZCZENIE GOSPODARCZE', 'pomieszczenie gospodarcze')], max_length=70, null=True, verbose_name='Rodzaj pomieszczenia'),
        ),
        migrations.AddField(
            model_name='room',
            name='window_in_room',
            field=models.CharField(choices=[('TAK', (('PŁ', 'na północ'), ('WSCH', 'na wschód'), ('PŁD', 'na południe'), ('ZACH', 'na zachód'))), ('NIE', (('BRAK', 'brak'),))], max_length=70, null=True, verbose_name='Ekspozycja okien'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='building_condition',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('WYREMONTOWANY DACH', 'wyremontowany dach'), ('TERMOMODERNIZACJA', 'budynek po termomodernizacji'), ('WYMIENIONE PIONY WODNE', 'instalacja wodno-kanalizacyjna wymieniona')], max_length=300, null=True, verbose_name='Prace przeprowadzone w budynku'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='flat_condition',
            field=models.CharField(choices=[('PO_REMONCIE', 'po remoncie'), ('DOBRY', 'dobry'), ('DO_REMONTU', 'do remontu')], max_length=30, null=True, verbose_name='Stan mieszkania'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='floor_area',
            field=models.PositiveIntegerField(help_text='m2', validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(1)], verbose_name='Metraż'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='how_high',
            field=models.PositiveIntegerField(help_text='cm', validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)], verbose_name='Wysokość pomieszczeń'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='how_many_flors',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)], verbose_name='Pięter w budynku'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='how_many_rooms',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Liczba pokoi'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='market',
            field=models.CharField(choices=[('WTÓRNY', 'wtórny'), ('PIERWOTNY', 'pierwotny')], max_length=30, null=True, verbose_name='Rynek'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='price',
            field=models.PositiveIntegerField(help_text='PLN', validators=[django.core.validators.MaxValueValidator(20000000), django.core.validators.MinValueValidator(1)], verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='type_of_building',
            field=models.CharField(choices=[('KAMIENICA', 'kamienicy'), ('BLOK', 'bloku'), ('SZEREGOWIEC', 'szeregowcu')], max_length=30, null=True, verbose_name='Rodzaj budynku'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='which_flor',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)], verbose_name='Kondygnacja'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='why_flat_change',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ZMIANA MIASTA', 'zmiany miasta'), ('ZMIANA NA WIEKSZE', 'zmiany na wieksze'), ('INNE', 'inne')], max_length=30, null=True, verbose_name='Sprzedaje z powodu'),
        ),
    ]
