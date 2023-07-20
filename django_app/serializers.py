from rest_framework import serializers 

from .models import Jihaz




class JihazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jihaz
        fields = '__all__'
