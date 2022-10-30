# Generated by Django 4.0.5 on 2022-06-21 17:19

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='around_facilities',
            field=models.CharField(choices=[('BD', 'BD')], help_text='Udogodnienia w budynku', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='around_security',
            field=models.CharField(choices=[('BD', 'BD')], help_text='Bezpieczeństwo okolicy', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='building_condition',
            field=models.CharField(choices=[('BD', 'BD')], help_text='Stan budynku', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='flat_condition',
            field=models.CharField(choices=[('PO_REMONCIE', 'po remoncie'), ('DOBRY', 'dobry'), ('DO_REMONTU', 'do remontu')], help_text='Stan mieszkania', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='flat_facilities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('WINDA', 'winda'), ('PODJAZD NA WÓZKI', 'podjazd na wózki'), ('WINDA DLA WÓZKÓW', 'winda dla wózków')], max_length=39, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='floor_area',
            field=models.IntegerField(default=666, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='how_high',
            field=models.IntegerField(default=666, help_text='Wysokość w cm', validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='how_many_flors',
            field=models.IntegerField(default=666, help_text='Ile pięter w budynku?', validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='how_many_levels',
            field=models.IntegerField(default=666, help_text='Ile pięter w mieszkaniu?', validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='how_many_rooms',
            field=models.IntegerField(default=666, help_text='Ilość pokoi', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='market',
            field=models.CharField(choices=[('WTÓRNY', 'wtórny'), ('PIERWOTNY', 'pierwotny')], help_text='Rynek', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='name_of_city',
            field=models.CharField(default=666, help_text='Miasto', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='name_of_street',
            field=models.CharField(default=666, help_text='Ulica', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='price',
            field=models.IntegerField(default=666, help_text='Cena', validators=[django.core.validators.MaxValueValidator(20000000), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='type_of_building',
            field=models.CharField(choices=[('BD', 'BD')], help_text='Rodzaj budynku', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='type_of_room',
            field=models.CharField(choices=[('SALON', 'salon'), ('SALON Z ANEKSEM', 'salon z aneksem'), ('POKOJ', 'pokoj'), ('KORYTARZ', 'korytarz'), ('LAZIENKA', 'lazienka'), ('TOALETA', 'wc'), ('ŁAZIENKA Z WC', 'lazienka z wc'), ('GARDEROBA', 'garderoba'), ('POMIESZCZENIE GOSPODARCZE', 'pomieszczenie gospodarcze')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='which_flor',
            field=models.IntegerField(default=666, help_text='Piętro w budynku', validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='why_flat_change',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ZMIANA MIASTA', 'zmiana miasta'), ('ZMIANA NA WIĘKSZE', 'zmiana na większe'), ('INNE', 'inne')], help_text='Powód zmiany nieruchomości', max_length=30, null=True),
        ),
    ]
