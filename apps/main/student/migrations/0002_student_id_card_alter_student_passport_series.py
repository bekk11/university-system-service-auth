# Generated by Django 4.1.4 on 2022-12-23 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ID_CARD',
            field=models.CharField(default=None, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='passport_series',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
