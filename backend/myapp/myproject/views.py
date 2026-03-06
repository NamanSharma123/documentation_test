from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

# Create your views here.

#List and create 
class CreateProductView(APIView):

    """
    GET -> LIST all products
    POST -> CREATE a new product
    """
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "message":"Products Fetched Successfully",
            "data":serializer.data
        },status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Product Created successfully",
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({
            "message":"Product Creation Failed",
            "errors" : serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    
    # Retrieve, Update (PUT), Partial Update (PATCH), Delete
class ProductDetailView(APIView):
    """
    GET -> RETRIVE Single Product
    PUT -> FUll Update (Replace)
    DELETE -> Delete a Product
    """

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
    
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response({
            "message" : "Product fetched successfully",
            "data": serializer.data
        },status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Product Updated Successfully",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        return Response({
            "message":"Product Updation Failed",
            "errors": serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response({
            "message":"Product Deleted Successfully"
        },status=status.HTTP_204_NO_CONTENT)
