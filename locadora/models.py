from django.db import models
from inventory.models import Carro, Loja
from django.contrib.auth import get_user_model
import random
import string

User = get_user_model()


# função que gera a hash do aluguel
def generate_random_hash(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))




class VendaCarro(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendas_efetuadas')
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    data_compra = models.DateField()
    data_retirada = models.DateField()

    def __str__(self):
        return f"Venda de {self.carro} para {self.cliente} na loja {self.loja} no dia {self.data_compra}"

    def save(self, *args, **kwargs):
        # Antes de salvar, atualize a disponibilidade do carro para False
        self.carro.disponibilidade = False
        self.carro.save()
        super().save(*args, **kwargs)


class Aluguel(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_retirada = models.DateTimeField()
    data_entrega = models.DateTimeField()
    hash_aleatoria = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.hash_aleatoria:
            self.hash_aleatoria = generate_random_hash(length=10)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket de Aluguel - {self.hash_aleatoria}"