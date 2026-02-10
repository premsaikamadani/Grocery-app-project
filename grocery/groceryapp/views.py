from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GrocerySerializer

# Create your views here.
@api_view(['POST'])
def grocery_create(request):
    serializer = GrocerySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)
    else:
        return Response(serializer.errors,status = 400)
