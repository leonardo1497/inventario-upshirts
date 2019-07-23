from inventario.models import Inventario
from .serializers import InventarioSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import JSONParser

# Create your views here.

class InventarioView(APIView):
    def get(self,request,format=None):
        queryset =Inventario.objects.all()
        serializer = InventarioSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = InventarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response,status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        inventario = Inventario.objects.get(id=pk)
        serializer = InventarioSerializer(inventario, data=data)
        if serializer.is_valid():
            inventarioUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk,format=None):
            inventario = get_object_or_404(Inventario.objects.all(), pk=pk)
            inventario.delete()
            return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)   
