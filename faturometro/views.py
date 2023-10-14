from django.http import JsonResponse
from django.db.models import Sum
from django.views import View
from .models import Venda


class Faturometro(View):
    def get(request, *args, **kwargs):
        total = Venda.objects.aggregate(total_vendas=Sum('valor'))
        return JsonResponse({'total_vendas': total['total_vendas']})
