from rest_framework import serializers
from .models import WELL

class wellSerializer(serializers.ModelSerializer):
    class Meta:
        model = WELL
        fields = ['WELL_ID', 'WELL_NAME', 'WELL_ALIAS_NAME']

 