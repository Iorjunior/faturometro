from django.http import JsonResponse
from django.db.models import Sum
from django.views import View
from .models import Venda


class Faturometro(View):
    def get(request, *args, **kwargs):
        painel = request.request.GET.get('id', '1')
        total = Venda.objects.filter(painel=int(painel)).aggregate(total_vendas=Sum('valor'))
        
        if total['total_vendas']:
            return JsonResponse({'total_vendas': total['total_vendas']})
        else:
            return JsonResponse({'total_vendas': '0.00'})
