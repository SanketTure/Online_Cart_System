# Generated by Django 4.1.7 on 2023-03-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_orderhistorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistorymodel',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
