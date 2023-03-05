# Generated by Django 4.1.7 on 2023-03-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_cartmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phoneNo', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
