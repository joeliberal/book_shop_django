from rest_framework.views import APIView
from rest_framework.response import Response
from book.models import Book
from .serializers import Bookserializer
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class ApiBook(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        ser = Bookserializer(books, many=True)

        return Response(ser.data)

    def post(self, request, format=None):
        ser = Bookserializer(data = request)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)



class AUDBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    ser = Bookserializer