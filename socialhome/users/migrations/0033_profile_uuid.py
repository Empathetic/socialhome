# Generated by Django 2.0.5 on 2018-08-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_make_profile_guid_and_handle_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(null=True, unique=True),
        ),
    ]