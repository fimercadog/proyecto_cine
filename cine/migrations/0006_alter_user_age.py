# Generated by Django 4.1.2 on 2022-10-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cine", "0005_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="age", field=models.CharField(max_length=3),
        ),
    ]
