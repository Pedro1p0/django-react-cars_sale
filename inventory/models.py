from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.



class Loja(models.Model):
    nome = models.CharField(max_length=255)

    localizacao = models.CharField(
        max_length=255,
        unique=True,
    )

    telefone = models.CharField(max_length=20)
    slug = models.SlugField(blank=True)

    def get_absolute_url(self):
        return reverse("websocket:dashboard_aluguel", kwargs={"slug": self.slug})
    

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        
        return self.nome


class Carro(models.Model):
    Marcas = (
        ("audi", "Audi"),
        ("bmw", "BMW"),
        ("ford", "Ford"),
        ("honda", "Honda"),
        ("mercedes", "Mercedes-Benz"),
        ("nissan", "Nissan"),
        ("toyota", "Toyota"),
        ("volkswagen", "Volkswagen"),
    )

    marca = models.CharField(
        max_length=50,
        choices=Marcas,
    )

    modelo = models.CharField(max_length=50)

    ano = models.IntegerField()

    cor = models.CharField(max_length=50)

    preco = models.DecimalField(max_digits=8, decimal_places=2)

    loja = models.ForeignKey("Loja", on_delete=models.CASCADE)

    disponibilidade = models.BooleanField(default=True)

    venda = models.BooleanField(default=False)

    locacao = models.BooleanField(default=False)

    placa = models.CharField(max_length=7)

    def __str__(self):
        if self.disponibilidade == True:
            Disp = "Disponivel"
        else:
            Disp = "Indisponivel"

        return f"{self.marca} {self.modelo} ({self.ano}) - {Disp} - Placa {self.placa}"

    