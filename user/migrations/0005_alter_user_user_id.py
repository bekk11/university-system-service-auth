# Generated by Django 4.1.4 on 2022-12-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_groups_alter_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='USER_ID',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]