from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from InventaryApp.models import Products
from InventaryApp.serializers import ProductSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        products = Products.objects.all()
        products_serializer=ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer=ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=Products.objects.get(ProductId=product_data['ProductId'])
        products_serializer=ProductSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        product=Products.objects.get(ProductId=id)
        product.delete()
        return JsonResponse("Deleted Successfully",safe=False)


def listProductsApi(request):
    if request.method=='GET':
        products = Products.objects.all()
        products_serializer = ProductSerializer(products,many=True)
        test = products_serializer.data
        listProducts = []
        for i in test:
            cont = 0
            for key, value in i.items():
                if cont == 1:
                    listProducts.append(value)
                cont += 1

        return JsonResponse(listProducts,safe=False)
    return JsonResponse("Solo se acepta petición GET",safe=False)


def productByName(request, string):
    if request.method=='GET':
        products = Products.objects.all()
        products_serializer=ProductSerializer(products,many=True)
        test = products_serializer.data
        for i in test:
            cont = 0
            for key, value in i.items():
                if cont == 1:
                    if value == string:
                        return JsonResponse(i,safe=False)
                    #listProducts.append(value)
                cont += 1

    return JsonResponse("Solo se acepta petición GET",safe=False)       
