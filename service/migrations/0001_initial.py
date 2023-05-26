# Generated by Django 4.2.1 on 2023-05-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DNAWindow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chromosome", models.CharField(max_length=10)),
                ("window_index", models.IntegerField()),
                ("start_position", models.BigIntegerField()),
                ("end_position", models.BigIntegerField()),
                ("enhancer_probability", models.FloatField()),
            ],
        ),
    ]