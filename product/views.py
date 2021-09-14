from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductListSerializer, CreateProductSerializer, ProductDetailSerializer


@api_view(['GET'])
def products_list(request):
    prods = Product.objects.all()
    serializer = ProductListSerializer(prods, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    prod = Product.object.get(id=pk)
    serializer = ProductDetailSerializer(prod)

# @api_view(['POST'])
# def create_product(request):
#     prod = Product.objects.all()
#     serializer = CreateProductSerializer(prod)
#
# @api_view(['PUT'])
# def product_update(request):
#     prod = Product.objects.all()
#     serializer = CreateProductSerializer(prod, name=True)
#     return Response(serializer.data)
#
# @api_view(['PATCH'])
# def product_

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'id'


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return CreateProductSerializer


