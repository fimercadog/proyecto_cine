# Generated by Django 4.1.2 on 2022-10-25 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cine", "0003_alter_client_name_alter_movie_director_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client", name="age", field=models.IntegerField(),
        ),
    ]
