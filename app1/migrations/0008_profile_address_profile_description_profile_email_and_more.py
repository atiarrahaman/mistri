# Generated by Django 4.1.3 on 2022-12-04 07:33

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(choices=[('alokbali', 'alokbali'), ('hajipur', 'hajipur'), ('karimpur', 'karipur'), ('chinispur', 'chinispur'), ('brammondi', 'brammondi'), ('beparipara', 'beparipara')], default=False, max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default='Write sommething About You', max_length=550),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=False, max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('electic', 'electic'), ('tv', 'tv'), ('mobail', 'mobail'), ('microwave', 'microwave'), ('carmechaig', 'carmechaig'), ('freezer', 'frezzer'), ('computer', 'computer'), ('printer', 'printer'), ('plumber', 'plumber'), ('color-prainter', 'color-prainter'), ('rajmisrti', 'rajmisrti'), ('katmistri', 'katmistri')], default=False, max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='write your Bio', max_length=150),
        ),
    ]
