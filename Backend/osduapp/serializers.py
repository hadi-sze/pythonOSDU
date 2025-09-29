from rest_framework import serializers
from .models import WELL
from .models import * 

class wellSerializer(serializers.ModelSerializer):
    class Meta:
        model = WELL
        fields = ['WELL_ID', 'WELL_NAME', 'WELL_ALIAS_NAME']

class FIELDSerializer(serializers.ModelSerializer):
     class Meta:
        model = FIELD
        db_table = 'FIELD'
        managed = True
        verbose_name = 'FIELD'
        verbose_name_plural = 'FIELD'
        fields = ['WELL_ID', 'FIELD_name', 'FIELD_ABBREVATION',"X_COORDINATE","Y_COORDINATE","CRIS_ID","CRS_NAME","IS_ACTIVE"]
class FieldSS(serializers.ModelSerializer):
     class Meta:
        model = FIELD
        fields = '__all__'
 