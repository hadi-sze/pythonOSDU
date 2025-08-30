from django.db import models

class Tempwell(models.Model):
    id=models.IntegerField(primary_key=id)
    wellname=models.CharField(max_length=255)
    componyname=models.CharField(max_length=255)
    amount=models.FloatField()

class shoretype(models.Model):    
    id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    isactive=models.BooleanField(default=True)
    measure=models.models.IntegerField(_(""))
# Create your models here.
class NIOC_Production_type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    is_available=models.BooleanField(default=True)

class NIOC_Production(models.Model):
    NIOC_Production_type=models.ForeignKey(NIOC_Production_type, on_delete=models.CASCADE)
    shore=models.ForeignKey(shoretype, on_delete=models.CASCADE)
    isactive=models.BooleanField(default=True)
    title=models.CharField(max_length=200)
    amount=models.CharField(max_length=100)
 
 
 
# /////////////////////////////////////////////////////
class Testidd(models.Model):    
    id = models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=200)
    isactive=models.BooleanField(default=True)
    

class testiddd(models.Model):
    id=models.AutoField(primary_key=True)
    testtype=models.ForeignKey(Testidd,on_delete=models.CASCADE)

# ////////////////////////////////////////////////////



#    //////////////////////////////////////////////////////////////////////
#  FIELD Calss
#    //////////////////////////////////////////////////////////////////////

class R_FIELD_TYPE(models.Model):
    R_FIELD_TYPE_ID = models.BigAutoField(primary_key=True)
    DISPLAY_NAME= models.CharField(max_length=200)
    LONG_NAME= models.CharField(max_length=200)
    SHORT_NAME= models.CharField(max_length=200)
    AVVRIVATION= models.CharField(max_length=200)
    COLOR_CODE= models.CharField(max_length=200)
    EFFECTIVE_DATE=models.DateTimeField()
    EXPIRED_DATE = models.DateTimeField()
    REMARK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    SOURCE_NAME = models.CharField(max_length=200)
    FILED_TYPE_NAME = models.CharField(max_length=200)

class FIELD(models.Model):
    FIELD_ID= models.BigAutoField(primary_key=True)
    FIELD_name = models.CharField(max_length=200)
    FIELD_TYPE_NAME = models.CharField(max_length=200)
    FIELD_ABBREVATION = models.CharField(max_length=200)
    XCOORDINATE =models.BigIntegerField(max_length=1000)
    Y_COORDINATE = models.BigIntegerField(max_length=1000)
    CRIS_ID
    CRS_NAME = models.CharField(max_length=200)
    REMARK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY = models.CharField(max_length=200)
    ROW_CREATED_DATE =models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY = models.CharField(max_length=200)
    SOURCE_NAME =  models.CharField(max_length=200)
    R_FIELD_TYPE_ID = models.ForeignKey(R_FIELD_TYPE,on_delete=models.CASCADE)
    CURRENT_ORG_UNIT_ID     = models.ForeignKey(CURRENT_ORG_UNIT,on_delete=models.CASCADE)
    FIELD=models.FileField()

class R_DATA_ACCESS_CATEGOTY(models.Model):
    R_DATA_ACCESS_CATEGOTY_ID= models.BigAutoField(primary_key=True)
    DATA_ACCESS_CATEGOTY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)




  

#    //////////////////////////////////////////////////////////////////////
#  FACILITY Calss
#    //////////////////////////////////////////////////////////////////////

class FACILITY(models.Model):
    FACILITY_ID=models.BigAutoField(primary_key=True)
#    //////////////////////////////////////////////////////////////////////
#  WELL Calss
#    //////////////////////////////////////////////////////////////////////

class WELL(models.Model):
    WELL_ID=models.BigAutoField(primary_key=True)
    WELL_NAME
    WELL_ALIAS_NAME
    FIELD_ID = models.ForeignKey(FIELD, on_delete= models.CASCADE)
    FIELD_NAME = 
    OFFSHORE =
    IS_ACTIVE = 
    WELL_OWNWER = 
    SPUD_DATE
    SPUD_DATE_TZ
    R_TIMEZONE_ID
    COMPLETION_DATE
    PRODUCTION_START_DATE
    X_COORDIBATE
    Y_COORDINATE
    CRS_ID
    CRX_NAME
    CURRENT_CLASS_ID
    WELL_CLASS
    DEEPEST_DEPTH = models.FloatField()
    max_tvd
    depth_






class WELL_ORG_UNIT(models.Model):
    WELL_ORG_UNIT_ID = models.BigAutoField(primary_key=True)
    WELL_ID = models.ForeignKey(WELL,on_delete=models.CASCADE)
    ORG_UNIT_ID = models.ForeignKey(ORG_UNIT,on_delete=models.CASCADE)

    FFECTIVE_DATE=models.DateTimeField()
    EXPIRED_DATE = models.DateTimeField()
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)




class R_ORG_UNIT_CATEGORY (models.Model):
    R_ORG_UNIT_CATEGORY_ID = models.BigAutoField(primary_key=True)
    ORG_UNIT_CATEGORY= models.CharField(max_length=200)
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)

class R_ORG_UNIT_TYPE (models.Model):
    R_ORG_UNIT_TYPE_ID = models.BigAutoField(primary_key=True)
    ORG_UNIT_TYPE= models.CharField(max_length=200)
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)



class ORG_UNIT (models.Model):
    ORG_UNIT_ID=models.BigAutoField(primary_key=True)
    ORG_UNIT_NAME = models.CharField
    R_ORG_UNIT_TYPE_ID=models.ForeignKey(R_ORG_UNIT_TYPE,on_delete=models.CASCADE)
    R_ORG_UNIT_CATEGORY_ID=models.ForeignKey(R_ORG_UNIT_CATEGORY,on_delete=models.CASCADE)
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)

class FIELD_ORG_UNIT (models.Model):
    FIELD_ORG_UNIT_ID=models.BigAutoField(primary_key=True)

    FIELD_ID = models.ForeignKey(FIELD,on_delete=models.CASCADE)
    ORD_UNIT_ID = models.ForeignKey(ORG_UNIT,on_delete=models.CASCADE)

    EFFECTIVE_DATE=models.DateTimeField()
    EXPIRED_DATE = models.DateTimeField()
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)



class FACILITY_ORG_UNIT (models.Model):
    FACILITY_ORG_UNIT_ID=models.BigAutoField(primary_key=True)
    ORG_UNIT_ID = models.ForeignKey(ORG_UNIT,on_delete=models.CASCADE)
    FACILITY_ID = models.ForeignKey(FACILITY,on_delete=models.CASCADE)

    FFECTIVE_DATE=models.DateTimeField()
    EXPIRED_DATE = models.DateTimeField()
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)





class HIERARCHY_LEVEL(models.Model):
    HIERARCHY_LEVEL_ID = models.BigAutoField(primary_key=True)
    HIERARCHY_DESC_ID= models.ForeignKey(HIERARCHY_LEVEL,)
    ORG_UNIT_ID = models.ForeignKey(ORG_UNIT,on_delete=models.CASCADE)
    #PAREINT_HIERARCHY_LEVEL_ID

    FFECTIVE_DATE=models.DateTimeField()
    EXPIRED_DATE = models.DateTimeField()
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)



 

 


