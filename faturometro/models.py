from django.db import models


class Venda(models.Model):
    PAINEL_CHOICE = (
        (1, 'DO CAMPO À MESA'),
        (2, 'SHOPPING COMPRE DO PEQUENO'),
    )
    valor =  models.DecimalField(verbose_name='Valor', max_digits=32, decimal_places=2, null=True, blank=True)
    painel = models.IntegerField(verbose_name='Painel', choices=PAINEL_CHOICE, null=False, blank=False, default=1)
    dt_created = models.DateTimeField(verbose_name='Data de criacao', auto_now=True)

    class Meta:
        verbose_name_plural = 'Vendas'
        ordering = ['-dt_created']

    def __str__(self):
        return f"{self.id} - {self.dt_created} - R${self.valor}"
