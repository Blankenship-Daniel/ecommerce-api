from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import BillingInfoSerializer, ShippingInfoSerializer
from .models import BillingInfo, ShippingInfo

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def billing_info_list(request):
    """
    List all billing infos, or create a new billing info.
    """
    if request.method == 'GET':
        billing_infos = BillingInfo.objects.all()
        serializer = BillingInfoSerializer(billing_infos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BillingInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def billing_info_detail(request, pk):
    """
    Retrieve, update or delete billing info.
    """
    try:
        billing_info = BillingInfo.objects.get(pk=pk)
    except BillingInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BillingInfoSerializer(billing_info)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BillingInfoSerializer(billing_info, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        billing_info.delete()
        return HttpResponse(status=204)

@csrf_exempt
def shipping_info_list(request):
    """
    List all shipping infos, or create a new shipping info.
    """
    if request.method == 'GET':
        shipping_infos = ShippingInfo.objects.all()
        serializer = ShippingInfoSerializer(shipping_infos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShippingInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def shipping_info_detail(request, pk):
    """
    Retrieve, update or delete shipping info.
    """
    try:
        shipping_info = ShippingInfo.objects.get(pk=pk)
    except ShippingInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShippingInfoSerializer(shipping_info)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShippingInfoSerializer(shipping_info, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shipping_info.delete()
        return HttpResponse(status=204)
