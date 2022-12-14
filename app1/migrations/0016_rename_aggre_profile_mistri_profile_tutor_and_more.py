# Generated by Django 4.1.3 on 2022-12-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_profile_add_more_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='aggre',
            new_name='mistri',
        ),
        migrations.AddField(
            model_name='profile',
            name='tutor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_tutor',
            field=models.BooleanField(default=False, verbose_name='is toutor'),
        ),
    ]