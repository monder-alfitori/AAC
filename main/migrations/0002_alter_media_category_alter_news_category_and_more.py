# Generated by Django 4.2.5 on 2023-10-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="category",
            field=models.CharField(
                choices=[
                    ("الملخصات", "highligts"),
                    ("الأرشيف", "archieve"),
                    ("لقاءات إعلامية", "meetings"),
                    ("الطائرة", "volleyball"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="category",
            field=models.CharField(
                choices=[
                    ("الفريق الأول", "first team"),
                    ("الطائرة", "volleyball"),
                    ("الأكاديمية", "academy"),
                    ("النادي", "club"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="position",
            field=models.CharField(
                choices=[
                    ("حارس مرمى", "GK"),
                    ("مدافع", "DF"),
                    ("متوسط ميدان", "MD"),
                    ("مهاجم", "ST"),
                    ("المدرب", "M"),
                    ("الطاقم الفني", "S"),
                ],
                max_length=100,
            ),
        ),
    ]
