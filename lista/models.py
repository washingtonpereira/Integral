from django.db import models


class Lista(models.Model):
    nome = models.CharField(max_length=255, unique=True,null=False, blank=False)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

