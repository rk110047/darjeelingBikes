# Generated by Django 3.1.3 on 2021-02-18 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
        ('vendor', '0003_auto_20210218_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_registraton_number', models.CharField(max_length=120)),
                ('year_of_registration', models.CharField(max_length=120)),
                ('date_of_registration', models.DateField()),
                ('engine_cc', models.CharField(max_length=120)),
                ('ABS', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], max_length=120)),
                ('bike_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.bikecompany')),
                ('bike_model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.bikemodel')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendorprofile')),
            ],
        ),
    ]
