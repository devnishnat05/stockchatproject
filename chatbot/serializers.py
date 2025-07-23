from rest_framework import serializers
from chatbot.models import Books 

class BooksSerializers(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

