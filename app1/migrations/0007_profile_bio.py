# Generated by Django 4.1.3 on 2022-12-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=False, max_length=150),
        ),
    ]
