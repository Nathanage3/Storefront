from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import DecimalField, Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.aggregates import Min, Max, Avg, Sum
from store.models import Product, OrderItem, Customer, Order, Collection
from tags.models import TaggedItem


def say_hello(request):
  #queryset = TaggedItem.objects.get_tags_for(Product, 1)
  """queryset = Product.objects.all()
  queryset[0] => caching
  list(queryset)
  """ 
  #collection = Collection(title_isull=False)
  """collection = Collection(pk=4)
     collection.delete()
  """

  #collection.objects.create(title='Video Games', featured_product_id=1)
  #Collection.objects.filter(pk=11).update(featured_product=None)
  with transaction.atomic(): 
   order = Order()
   order.customer_id = 1
   order.save()

   item = OrderItem()
   item.order = order
   item.product_id = 1
   item.quantity = 1
   item.unit_price = 10
   item.save()


  



  return render(request, 'hello.html')
 