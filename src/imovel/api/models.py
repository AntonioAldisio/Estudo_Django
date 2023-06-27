from django.db import models


class Imovel(models.Model):
    codigo_imovel = models.IntegerField(primary_key=True)
    limite_hospedes = models.IntegerField()
    quantidade_banheiros = models.IntegerField()
    aceita_animais = models.BooleanField()
    valor_limpeza = models.DecimalField(max_digits=8, decimal_places=2)
    data_ativacao = models.DateField(auto_now_add=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo_imovel
