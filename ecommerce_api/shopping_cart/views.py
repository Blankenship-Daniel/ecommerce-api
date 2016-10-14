from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import ShoppingCartSerializer, ShoppingCartProductSerializer
from .models import ShoppingCart, ShoppingCartProduct

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def shopping_cart_list(request):
    """
    List all shopping cart items, or create a new shopping cart.
    """
    if request.method == 'GET':
        shopping_carts = ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(shopping_carts, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShoppingCartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def shopping_cart_detail(request, pk):
    """
    Retrieve, update or delete a shopping cart.
    """
    try:
        shopping_cart = ShoppingCart.objects.get(pk=pk)
    except ShoppingCart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShoppingCartSerializer(shopping_cart)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShoppingCartSerializer(shopping_cart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shopping_cart.delete()
        return HttpResponse(status=204)

@csrf_exempt
def shopping_cart_product_list(request):
    """
    List all shopping cart products, or create a new shopping cart product.
    """
    if request.method == 'GET':
        shopping_cart_products = ShoppingCartProduct.objects.all()
        serializer = ShoppingCartProductSerializer(shopping_cart_products, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShoppingCartProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def shopping_cart_product_detail(request, pk):
    """
    Retrieve, update or delete shopping cart products.
    """
    try:
        shopping_cart_product = ShoppingCartProduct.objects.get(pk=pk)
    except ShoppingCartProduct.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShoppingCartProductSerializer(shopping_cart_product)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShoppingCartProductSerializer(shopping_cart_product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shopping_cart_product.delete()
        return HttpResponse(status=204)
