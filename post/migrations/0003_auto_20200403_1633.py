# Generated by Django 3.0.4 on 2020-04-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200403_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(max_length=600, null=True),
        ),
    ]