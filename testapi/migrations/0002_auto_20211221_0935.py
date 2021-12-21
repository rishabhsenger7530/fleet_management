# Generated by Django 3.2.8 on 2021-12-21 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMotor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor_type', models.CharField(choices=[('Hybrid', 'Hybrid'), ('Electric_Motor', 'Electric_Motor')], max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='car_motor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.carmotor'),
        ),
    ]