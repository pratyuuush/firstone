# Generated by Django 3.0.4 on 2020-04-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200403_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(max_length=100, null=True),
        ),
    ]