from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from store.models import Product, OrderItem, Customer, Order



def say_hello(request):
 queryset =  Product.objects.aggregate(Count('id'))
 context = {
        'name': 'Sisay',
        'product': queryset
 }
 return render(request, 'hello.html', context)
 