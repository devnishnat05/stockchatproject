from django.shortcuts import render
from rest_framework import viewsets
from .models import Books
from chatbot.serializers import BooksSerializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


# Create your views here.
