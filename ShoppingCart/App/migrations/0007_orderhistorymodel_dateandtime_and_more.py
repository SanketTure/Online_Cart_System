# Generated by Django 4.1.7 on 2023-03-04 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_orderhistorymodel_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistorymodel',
            name='dateAndTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderhistorymodel',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
