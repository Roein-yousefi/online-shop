# Generated by Django 5.0.7 on 2024-09-21 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 21, 9, 54, 7, 486655, tzinfo=datetime.timezone.utc)),
        ),
    ]
