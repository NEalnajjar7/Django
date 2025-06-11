from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer


# Functional Api views
@api_view(['GET'])
def product_list_functional(request):
    products= Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['Post'])
def product_create_functional(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class-based 

class ProductListClass(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Generic 

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


from django.shortcuts import render
#render for funcional
def product_template_functional(request):
    return render(request, 'product_form.html')

#render for class 

def product_template_class(request):
    return render(request, 'product_form.html', {'api_type': 'class'})

#render for generic
def product_template_generic(request):
    return render(request, 'product_form.html' , {'api_type':'generic'})


from django.shortcuts import render

def product_template_view(request):
    return render(request, 'product_form.html')


from django.shortcuts import get_object_or_404

class ProductDetailClass(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)



    def post(self, request, pk):
        product = get_object_or_404(product,pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    