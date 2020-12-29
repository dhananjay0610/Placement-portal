# Generated by Django 3.1.4 on 2020-12-12 09:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_profile_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
