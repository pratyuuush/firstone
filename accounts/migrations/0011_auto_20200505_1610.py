# Generated by Django 3.0.5 on 2020-05-05 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_rating_reciever'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_recieved', to=settings.AUTH_USER_MODEL),
        ),
    ]
