# Generated by Django 4.2.7 on 2023-12-25 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dr_name', models.CharField(max_length=200)),
                ('Patient_name', models.CharField(max_length=200)),
                ('profile', models.ImageField(default='', upload_to='profile')),
                ('saved_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
