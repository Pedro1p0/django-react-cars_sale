# Generated by Django 4.1.9 on 2023-06-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0003_carro_placa"),
    ]

    operations = [
        migrations.AddField(
            model_name="loja",
            name="slug",
            field=models.SlugField(blank=True),
        ),
    ]
