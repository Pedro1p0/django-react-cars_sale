from typing import Any, Optional
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    UserManager,
    AbstractUser,
)
from django.db import models
from django.db.models.query import QuerySet
from inventory.models import Loja
from django.db.models.signals import post_save 
from django.dispatch import receiver


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = (
            "ADMIN",
            "Admin",
        )
        CLIENTE = (
            "CLIENTE",
            "Cliente",
        )
        FUNCIONARIO = "FUNCIONARIO", "Funcionario"

    base_role = Role.ADMIN

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
    )

    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg, **kwargs)


class ClienteManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.CLIENTE)


class Cliente(CustomUser):
    base_role = CustomUser.Role.CLIENTE
    cliente = ClienteManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Apenas para clientes"

@receiver(post_save, sender = Cliente)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CLIENTE":
        ClienteProfile.objects.create(user=instance)

class ClienteProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cliente_id = models.IntegerField(null=True, blank=True)


class FuncionarioManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.FUNCIONARIO)


class Funcionario(CustomUser):
    base_role = CustomUser.Role.FUNCIONARIO
    cliente = FuncionarioManager()


    class Meta:
        proxy = True

    def welcome(self):
        return "Apenas para funcionarios"

@receiver(post_save, sender = Funcionario)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "FUNCIONARIO":
        funcionario_profile, _ = FuncionarioProfile.objects.get_or_create(user=instance)

class FuncionarioProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cliente_id = models.IntegerField(null=True, blank=True)
    loja = models.ForeignKey(Loja, blank=True, null = True, on_delete= models.CASCADE)


    