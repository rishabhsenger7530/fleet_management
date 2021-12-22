# Generated by Django 3.2.8 on 2021-12-22 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carmodel', to='car.carmanufacurer'),
        ),
    ]
