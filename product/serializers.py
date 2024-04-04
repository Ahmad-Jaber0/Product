from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def validate_name(self, value):

        if not value.isalpha():
            raise serializers.ValidationError("Name must contain only alphabetic characters.")
        return value    

class offerSerializer(serializers.ModelSerializer):
    class Meta:
        model = offer
        fields = '__all__'
