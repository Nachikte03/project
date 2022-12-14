# Generated by Django 4.1.1 on 2022-10-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabBooking',
            fields=[
                ('bookingid', models.CharField(default=1, max_length=30)),
                ('ticketNo', models.CharField(default='Review', max_length=30, primary_key=True, serialize=False)),
                ('journeyDate', models.CharField(max_length=30)),
                ('routeValue', models.CharField(max_length=30)),
                ('route', models.CharField(max_length=70)),
                ('seatNo', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=70)),
                ('mobileNo', models.CharField(blank=True, max_length=10, null=True)),
                ('pickupTime', models.CharField(max_length=10)),
                ('pickupValue', models.CharField(max_length=30)),
                ('pickupLocation', models.CharField(max_length=70)),
                ('droppingLocation', models.CharField(blank=True, max_length=70, null=True)),
                ('droppingValue', models.CharField(max_length=30)),
                ('luggage', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
