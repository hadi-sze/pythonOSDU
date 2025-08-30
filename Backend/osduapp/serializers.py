from rest_framework import serializers
from .models import well

class wellSerializer(serializers.ModelSerializer):
    class Meta:
        model = well
        fields = ['id', 'wellname', 'componyname', 'amount']

 