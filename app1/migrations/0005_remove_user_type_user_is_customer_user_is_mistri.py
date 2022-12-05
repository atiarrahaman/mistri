# Generated by Django 4.1.3 on 2022-12-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='is customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_mistri',
            field=models.BooleanField(default=False, verbose_name='is mistri'),
        ),
    ]
