# Generated by Django 4.1.9 on 2023-05-19 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0002_carro_locacao_carro_venda"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("locadora", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aluguel",
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
                ("data_retirada", models.DateTimeField()),
                ("data_entrega", models.DateTimeField()),
                ("hash_aleatoria", models.CharField(max_length=10, unique=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "loja",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="inventory.loja"
                    ),
                ),
            ],
        ),
    ]
