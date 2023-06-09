# Generated by Django 4.1.4 on 2022-12-14 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('type_education', models.CharField(choices=[['FULL_TIME', 'FULL_TIME'], ['EVENING', 'EVENING'], ['DISTANCE_LEARNING', 'DISTANCE_LEARNING']], max_length=20)),
                ('language', models.CharField(choices=[['ENGLISH', 'ENGLISH'], ['UZBEK', 'UZBEK'], ['RUSSIAN', 'RUSSIAN'], ['KOREAN', 'KOREAN']], max_length=10)),
                ('level', models.SmallIntegerField(default=1, null=True)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='faculty.faculty')),
            ],
        ),
    ]
