# Generated by Django 2.1.7 on 2019-04-01 13:40

import app_product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0002_auto_20190401_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='bigimg',
            field=models.ImageField(blank=True, upload_to=app_product.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='app',
            name='smallPic',
            field=models.ImageField(blank=True, upload_to=app_product.models.user_directory_path),
        ),
    ]
