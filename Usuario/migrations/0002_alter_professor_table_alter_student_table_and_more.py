# Generated by Django 4.1.7 on 2023-03-22 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='professor',
            table='Professor',
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]