# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0006_auto_20180308_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accident_location', models.CharField(max_length=20)),
                ('accident_cause', models.CharField(max_length=20)),
                ('no_persons_injured', models.IntegerField()),
                ('accident_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PollutionCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('next_service_data', models.DateField()),
                ('total_distance', models.IntegerField()),
                ('pollution_status', models.CharField(choices=[('GOOD', 'Good'), ('BAD', 'Bad')], default=1, max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicledetails',
            name='vehicle_class',
            field=models.CharField(choices=[('AMBULANCE', 'Ambulance'), ('CRANE', 'Crane'), ('FIRE FIGHTER', 'Fire Fighter'), ('HEAVY GOODS VEHICLE', 'Heavy Goods Vehicle'), ('L.M.V.(CAR)', 'L.M.V.(Car)'), ('L.M.V.(JEEP/GYPSY)', 'L.M.V.(Jeep/GYPSY)'), ('L.M.V.(VAN)', 'L.M.V.(Van)'), ('MOTOR CYCLE', 'Motor Cycle'), ('THREE WHEELER', 'Three Wheeler'), ('TRACTOR', 'Tractor')], default=8, max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicledetails',
            name='vehicle_type',
            field=models.CharField(choices=[('PRIVATE', 'Private'), ('GOODS', 'Goods'), ('PASSENGER', 'Passenger'), ('SPECIAL', 'Special')], default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='pollutioncenter',
            name='v_no',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mud.VehicleDetails'),
        ),
        migrations.AddField(
            model_name='policeofficer',
            name='vehicle_no',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mud.VehicleDetails'),
        ),
    ]
