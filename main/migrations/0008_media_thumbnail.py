# Generated by Django 4.2.5 on 2023-10-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_player_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="media",
            name="thumbnail",
            field=models.ImageField(null=True, upload_to="images/%y/%m/%d"),
        ),
    ]
