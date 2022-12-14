# Generated by Django 4.1.3 on 2022-12-09 15:23

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_profile_add_more_clases_profile_clases_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='add_more_subject',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('c1', 'claas 1'), ('c2', 'claas 2'), ('c3', 'claas 3'), ('c4', 'claas 4'), ('c5', 'claas 5'), ('c6', 'claas 6'), ('c7', 'claas 7'), ('c8', 'claas 8'), ('c9', 'claas 9'), ('c10', 'claas 10'), ('c11', 'Inter First year'), ('c12', 'Inter Second Year')], default=False, max_length=25, null=True),
        ),
    ]