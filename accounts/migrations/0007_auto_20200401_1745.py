# Generated by Django 3.0.4 on 2020-04-01 12:15

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200401_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
