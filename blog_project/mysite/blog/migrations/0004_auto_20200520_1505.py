# Generated by Django 3.0.3 on 2020-05-20 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200519_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 9, 35, 38, 338528, tzinfo=utc)),
        ),
    ]
