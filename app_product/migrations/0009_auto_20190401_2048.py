# Generated by Django 2.1.7 on 2019-04-01 18:48

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0008_auto_20190401_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='keywords',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]