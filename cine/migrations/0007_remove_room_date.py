# Generated by Django 4.1.2 on 2022-10-29 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cine", "0006_alter_user_age"),
    ]

    operations = [
        migrations.RemoveField(model_name="room", name="date",),
    ]
