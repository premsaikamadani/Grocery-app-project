from django.shortcuts import render
from .models import Grocery
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GrocerySerializer

@api_view(['POST'])
def grocery_create(request):
    serializer = GrocerySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def grocery_list(request):
    groceries = Grocery.objects.all()
    serializer = GrocerySerializer(groceries, many=True)
    return Response(serializer.data,status=200)
