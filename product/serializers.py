from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class offerSerializer(serializers.ModelSerializer):
    class Meta:
        model = offer
        fields = '__all__'
