# Generated by Django 3.0.4 on 2020-03-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_post_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
