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
#  R CLASES
#    //////////////////////////////////////////////////////////////////////

class R_DATA_ACCESS_CATEGORY (models.Model):
    R_DATA_ACCESS_CATEGORY_id =  models.AutoField(primary_key=True)
    R_DATA_ACCESS_CATEGORY =models.CharField(max_length=200)
    SHORT_NAME=models.CharField(max_length=200)
    LONH_NAME = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    REMARK = models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    
    
#    //////////////////////////////////////////////////////////////////////
#  FIELD Calss
#    //////////////////////////////////////////////////////////////////////

class CARTOREFERENCESYSTEM(models.Model):
    CRS_ID = models.BigAutoField(primary_key=True)
    CRS_NAME=models.CharField(max_length=200)
    CRS_TYPE = models.CharField(max_length=200)
    GEODETIC_SOURCE = models.CharField(max_length=200)
    PROHECTION_TYPE = models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    LONH_NAME = models.CharField(max_length=200)
    SHORT_NAME=models.CharField(max_length=200)
    REMARK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)

class R_TIMEZONE(models.Model):
    R_TIMEZONE_ID = models.BigAutoField(primary_key=True)
    TIMEZONE =  models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    LONH_NAME = models.CharField(max_length=200)
    SHORT_NAME=models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)

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
    
    CRIS_ID = models.name = models.ForeignKey('CARTOREFERENCESYSTEM', CARTOREFERENCESYSTEM, on_delete=models.CASCADE)
    CRS_NAME = models.CharField(max_length=200)
    REMARK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY = models.CharField(max_length=200)
    ROW_CREATED_DATE =models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY = models.CharField(max_length=200)
    SOURCE_NAME =  models.CharField(max_length=200)
    R_FIELD_TYPE_ID = models.ForeignKey(R_FIELD_TYPE,on_delete=models.CASCADE)
    CURRENT_ORG_UNIT_ID   = models.ForeignKey(CURRENT_ORG_UNIT,on_delete=models.CASCADE)
    FIELD=models.FileField()

class R_DATA_ACCESS_CATEGOTY(models.Model):
    R_DATA_ACCESS_CATEGOTY_ID= models.BigAutoField(primary_key=True)
    DATA_ACCESS_CATEGOTY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)



class FIELD_ORG_UNIT(models.Model):
    FIELD_ORG_UNIT_ID = models.BigAutoField(primary_key=True)
    FILED_ID = models.ForeignKey(FIELD,MODE)
    ORG_UNIT_ID = models.DateTimeField()
    EFFECTIVE_DATE = models.DateTimeField()
    EXPIRE_DATE = models.DateTimeField()
    REMARK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY = models.CharField(max_length=200)
    ROW_CREATED_DATE = models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
  

#    //////////////////////////////////////////////////////////////////////
#  FACILITY Calss
#    //////////////////////////////////////////////////////////////////////

class FACILITY(models.Model):
    FACILITY_ID=models.BigAutoField(primary_key=True)

##    //////////////////////////////////////////////////////////////////////
#
#  WELL Calss
#
#
# WELL: A well is the location on the surface of the earth or 
# sea bed where the drill bit is planned to penetrate or
# does penetrate the earth to establish or 
# rework a well. The well will be the same with Well Origin in PPDM.
##    //////////////////////////////////////////////////////////////////////

class R_SOURCE(models.Model):
    R_SOURCE_ID =models.BigAutoField(primary_key=True) 
    DISPLAY_NAME = models.CharField(max_length=200)
    ABBREVIATION = models.CharField(max_length=200)
    LONG_NAME = models.CharField(max_length=200)
    SHOTR_NAME = models.CharField(max_length=200)
    COLOR_CODE = models.CharField(max_length=200)
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    IS_ACTIVE=models.BooleanField(default=True)
    REMARK =  models.CharField(max_length=200)

class R_WELL_STATUS_TYPE (models.Model):
   R_WELL_STATUS_TYPE_ID =models.BigAutoField(primary_key=True) 
   R_WELL_STATUS_TYPE = models.CharField(max_length=200)
   R_SOURCE_ID =models.ForeignKey(R_SOURCE,on_delete=models.CASCADE) 
   IS_ACTIVE=models.BooleanField(default=True)
   REMARK =  models.CharField(max_length=200)
    
   LONG_NAME = models.CharField(max_length=200)
   SHOTR_NAME = models.CharField(max_length=200)
    
   ROW_CHANGED_DATE = models.DateTimeField()
   ROW_CHANEGED_BY= models.CharField(max_length=200)
   ROW_CREATED_BY= models.CharField(max_length=200)
   ROW_CREATED_DATE=models.DateTimeField()
   



class R_WELL_DATUM_TYPE(models.Model):
    R_WELL_DATUM_TYPE_ID  =models.BigAutoField(primary_key=True) 
    R_WELL_DATUM_TYPE= models.CharField(max_length=200)
    ABBREVIATION = models.CharField(max_length=200)
    LONG_NAME = models.CharField(max_length=200)
    SHOTR_NAME = models.CharField(max_length=200)
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    IS_ACTIVE=models.BooleanField(default=True)
    REMARK =  models.CharField(max_length=200)

class R_WELL_CLASS():
    R_WELL_CLASS_ID  =models.BigAutoField(primary_key=True) 
    WELL_CLASS= models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    LONG_NAME = models.CharField(max_length=200)
    REMARK =  models.CharField(max_length=200)

class R_WELL_STATUS():
    R_WELL_STATUS_ID  =models.BigAutoField(primary_key=True) 
    R_WELL_STATUS= models.CharField(max_length=200)
    R_WELL_STATUS_TYPE_ID = models.ForeignKey(r_wel)


    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    LONG_NAME = models.CharField(max_length=200)
    REMARK =  models.CharField(max_length=200)



class WELL(models.Model):
    WELL_ID=models.BigAutoField(primary_key=True)
    UWI = models.CharField(max_length=200)
    WELL_NAME = models.CharField(max_length=200)
    WELL_ALIAS_NAME =  models.CharField(max_length=200)
    FIELD_ID = models.ForeignKey(FIELD, on_delete= models.CASCADE)
    FIELD_NAME = models.CharField(max_length=200)
    OFFSHORE_IND = models.BooleanField()
    IS_ACTIVE = models.BooleanField()
    WELL_OWNWER = models.CharField(max_length=200)
    SPUD_DATE = models.ForeignKey(R_TIMEZONE, on_delete= models.CASCADE)
    SPUD_DATE_TZ = models.CharField(max_length=200) #// TI,E
    R_TIMEZONE_ID = models.ForeignKey(R_TIMEZONE,on_delete=models.CASCADE)
    COMPLETION_DATE = models.DateTimeField()
    PRODUCTION_START_DATE = models.DateTimeField()
    X_COORDIBATE = models.DecimalField()
    Y_COORDINATE = models.DecimalField()
    CRS_ID = models.ForeignKey(CARTOREFERENCESYSTEM,on_delete=models.CASCADE)
    CRX_NAME = models.CharField(max_length=200,blank=True, null=True)
    CURRENT_CLASS_ID = models.ForeignKey(R_WELL_CLASS,on_delete=models.CASCADE)
    WELL_CLASS =  models.ForeignKey(R_WELL_CLASS,on_delete=models.CASCADE)  #class name
    DEEPEST_DEPTH = models.FloatField()
    MAX_TVD = models.DecimalField()
    DEPTH_DATUM_ID = models.ForeignKey(R_WELL_DATUM_TYPE,on_delete=models.CASCADE)
    dDEPTH_DATUM = models.ForeignKey(R_WELL_DATUM_TYPE,on_delete=models.CASCADE)  #class name

    DEPTH_DATUM_ELEV = models.DecimalField()
    GROUND_ELEV  = models.DecimalField()
    ROW_CREATED_BY = models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY = models.CharField(max_length=200)
    
    BOTTOM_HOLE_X_LON = models.DecimalField()
    BOTTOM_HOLE_Y_LAT =  models.DecimalField()
    ABANDONMENT_DATE = models.DateTimeField()
    EXPIRY_DATE = models.DateTimeField()
    FAULTED_IND = models.models.IntegerField(blank=True, null=True)
    FINAL_DRILL_DATE =  models.DateTimeField()
    LOG_TD = models.DateTimeField()
    NET_PAY = models.DateTimeField()
    OPERATOR =  models.CharField(max_length=200)
    PLOT_NAME  = models.CharField(max_length=200)
    PLUGBACK_DEPTH  = models.DateTimeField()
    R_WELL_PROFILE_ID = models.ForeignKey(R_WELL_STATUS, on_delete=models.CASCADE)
    WELL_PROFILE = models.ForeignKey(R_WELL_STATUS, on_delete=models.CASCADE)
    WATER_ACOUSTIC_VEL =  models.DateTimeField()
    WATER_DEPTH =  models.DecimalField()
    WATER_DEPTH_DATUM =  models.CharField(max_length=200)
    IS_VIRTUAL = models.BooleanField()
   
    R_DATA_ACCESS_CATEGORY_ID = models.ForeignKey(R_DATA_ACCESS_CATEGORY)


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



 

 


