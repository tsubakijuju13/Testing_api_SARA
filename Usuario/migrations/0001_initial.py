# Generated by Django 4.1.7 on 2023-03-22 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('identification', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('cellphone', models.CharField(default='0000000000', max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academy_program', models.IntegerField()),
                ('code_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.user')),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=40)),
                ('code_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.user')),
            ],
            options={
                'db_table': 'Professor',
            },
        ),
    ]
