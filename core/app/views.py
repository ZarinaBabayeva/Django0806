from django.shortcuts import render
from django.db.models import FloatField , F
from django.db.models.functions import Coalesce
from app.models import *
# Create your views here.
def list_view(request):
    context = {
        "products": Product.objects.annotate(
            discount_prices = Coalesce ('discount_price',0,output_field=FloatField()),
            total_price = F('price')-F('discount_prices')
        ),
    }
    return render(request, 'pages/list.html', context)
def list_2_view(request):
    context = {
        "products": Product.objects.annotate(
            discount_prices = Coalesce ('discount_price',0,output_field=FloatField()),
            total_price = F('price')-F('discount_prices')
        ),
    }
    return render(request, 'pages/list_2.html', context)