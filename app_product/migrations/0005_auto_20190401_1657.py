# Generated by Django 2.1.7 on 2019-04-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0004_auto_20190401_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='Fakultaet',
            field=models.CharField(choices=[('FK00', 'General'), ('FK01', 'Fakultät 01'), ('FK02', 'Fakultät 02'), ('FK03', 'Fakultät 03'), ('FK04', 'Fakultät 04'), ('FK05', 'Fakultät 05'), ('FK06', 'Fakultät 06'), ('FK07', 'Fakultät 07'), ('FK08', 'Fakultät 08'), ('FK09', 'Fakultät 09'), ('FK10', 'Fakultät 10'), ('FK11', 'Fakultät 11'), ('FK12', 'Fakultät 12'), ('FK13', 'Fakultät 13'), ('FK14', 'Fakultät 14')], default='FK07', max_length=4),
        ),
        migrations.AlterField(
            model_name='app',
            name='typOfAccount',
            field=models.CharField(choices=[('ST', 'Student'), ('SA', 'Staff'), ('PR', 'Professor'), ('Fr', 'Externer Student'), ('All', 'Non Type')], default='ST', max_length=2),
        ),
    ]
