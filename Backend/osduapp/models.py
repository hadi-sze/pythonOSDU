from django.db import models

# class Tempwell(models.Model):
#     id=models.IntegerField(primary_key=id)
#     wellname=models.CharField(max_length=255)
#     componyname=models.CharField(max_length=255)
#     amount=models.FloatField()

# class shoretype(models.Model):    
#     id = models.IntegerField(primary_key=True)
#     title=models.CharField(max_length=200)
#     isactive=models.BooleanField(default=True)
#     measure=models.IntegerField()
# # Create your models here.
# class NIOC_Production_type(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name=models.CharField(max_length=255)
#     is_available=models.BooleanField(default=True)

# class NIOC_Production(models.Model):
#     NIOC_Production_type=models.ForeignKey(NIOC_Production_type, on_delete=models.CASCADE)
#     shore=models.ForeignKey(shoretype, on_delete=models.CASCADE)
#     isactive=models.BooleanField(default=True)
#     title=models.CharField(max_length=200)
#     amount=models.CharField(max_length=100)
 
 
 
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
class R_EQUIPMENT_CATALOGUE (models.Model):
    R_EQUIPMENT_CATALOGUE_ID= models.AutoField(primary_key=True)
    R_EQUIPMENT_CATALOGUE = models.CharField(max_length=200)
    SHORT_NAME=models.CharField(max_length=200)
    LONH_NAME = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    REMARK = models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)


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


class R_EQUIPMENT_TYPE(models.Model):
    R_EQUIPMENT_TYPE_ID = models.AutoField(primary_key=True)
    EQUIPMENT_TYPE = models.CharField(max_length=200)
    R_EQUIPMENT_CATALOGUE_ID = models.ForeignKey(R_EQUIPMENT_CATALOGUE,on_delete=models.CASCADE)
    SHORT_NAME=models.CharField(max_length=200)
    LONH_NAME = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    REMARK = models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)



class R_EQUIPMENT_SUB_TYPE (models.Model):
    RR_EQUIPMENT_SUB_TYPE_ID =  models.AutoField(primary_key=True)
    R_EQUIPMENT_SUB_TYPE =models.CharField(max_length=200)
    SHORT_NAME=models.CharField(max_length=200)
    LONH_NAME = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    REMARK = models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    
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
    
class R_DATA_ACCESS_CATEGOTY(models.Model):
    R_DATA_ACCESS_CATEGOTY_ID= models.BigAutoField(primary_key=True)
    DATA_ACCESS_CATEGOTY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)



#    //////////////////////////////////////////////////////////////////////
#  
#     FIELD Calss
#
#
# FIELD: A geographical area defined for administrative and legal purposes. 
# The field name refers to the surface area, although at times it may refer to both the surface and 
# the underground productive zones. 
# In the United States a field is often an area consisting of a single reservoir or multiple reservoirs
#  all grouped on, or related to, 
# the same individual geological structural feature and/or stratigraphic condition.
#  Fields are usually defined at a province/state level but possibly are done at the district level.
#    //////////////////////////////////////////////////////////////////////



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
    FIELD_ABBREVATION = models.CharField(max_length=200)
    X_COORDINATE =models.DecimalField(max_length=10,decimal_places=2,max_digits=10 , blank=True, null=True)
    Y_COORDINATE = models.DecimalField(max_length=10,decimal_places=2,max_digits=10 , blank=True, null=True)
    CRIS_ID = models.name = models.ForeignKey(CARTOREFERENCESYSTEM, on_delete=models.CASCADE)
    CRS_NAME = models.CharField(max_length=200)
    REMARK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY = models.CharField(max_length=200)
    ROW_CREATED_DATE =models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY = models.CharField(max_length=200)
    SOURCE_NAME =  models.CharField(max_length=200)
    R_FIELD_TYPE_ID = models.ForeignKey(R_FIELD_TYPE,on_delete=models.CASCADE)
    





class FIELD_ORG_UNIT(models.Model):
    FIELD_ORG_UNIT_ID = models.BigAutoField(primary_key=True)
    FILED_ID = models.ForeignKey(FIELD,on_delete=models.CASCADE)
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
   IS_ACTIVE=models.BooleanField(default=True)
   REMARK =  models.CharField(max_length=200)
   LONG_NAME = models.CharField(max_length=200)
   SHOTR_NAME = models.CharField(max_length=200)
   ROW_CHANGEDCS_DATE = models.DateTimeField()
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

class R_WELL_CLASS(models.Model):
    R_WELL_CLASS_ID  =models.BigAutoField(primary_key=True) 
    WELL_CLASS= models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    LONG_NAME = models.CharField(max_length=200)
    REMARK =  models.CharField(max_length=200)

class R_WELL_STATUS(models.Model):
    R_WELL_STATUS_ID  =models.BigAutoField(primary_key=True) 
    R_WELL_STATUS= models.CharField(max_length=200)
    R_WELL_STATUS_TYPE_ID = models.ForeignKey(R_WELL_STATUS_TYPE,on_delete=models.CASCADE)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    LONG_NAME = models.CharField(max_length=200)
    REMARK=  models.CharField(max_length=200)



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
    SPUD_DATE = models.DateField()
    SPUD_DATE_TZ = models.CharField(max_length=200) #// TI,E
    R_TIMEZONE_ID = models.ForeignKey(R_TIMEZONE,on_delete=models.CASCADE)
    COMPLETION_DATE = models.DateTimeField()
    PRODUCTION_START_DATE = models.DateTimeField()
                       
    X_COORDIBATE = models.DecimalField(max_length=10,decimal_places=2,max_digits=10 , blank=True, null=True)
    Y_COORDINATE = models.DecimalField(max_length=10,decimal_places=2, max_digits=10 , blank=True, null=True)
    CRS_ID = models.ForeignKey(CARTOREFERENCESYSTEM,on_delete=models.CASCADE)
    CRX_NAME = models.CharField(max_length=200,blank=True, null=True)
    CURRENT_CLASS_ID = models.ForeignKey(R_WELL_CLASS,on_delete=models.CASCADE)
    #WELL_CLASS =  models.ForeignKey(R_WELL_CLASS,on_delete=models.CASCADE)  #class name
    DEEPEST_DEPTH = models.FloatField(max_length=5)
    DEPTH_DATUM_ID = models.ForeignKey(R_WELL_DATUM_TYPE,on_delete=models.CASCADE)
    DEPTH_DATUM = models.CharField(max_length=200)





    DEPTH_DATUM_ELEV = models.DecimalField(max_length=10,decimal_places=5,max_digits=10)
    ROW_CREATED_BY = models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY = models.CharField(max_length=200)
    
    BOTTOM_HOLE_X_LON = models.DecimalField(max_length=5,decimal_places=2,max_digits=10)
    BOTTOM_HOLE_Y_LAT =  models.DecimalField(max_length=5,decimal_places=2,max_digits=10)
    ABANDONMENT_DATE = models.DateTimeField()
    EXPIRY_DATE = models.DateTimeField()
    FAULTED_IND = models.IntegerField(blank=True, null=True)
    FINAL_DRILL_DATE =  models.DateTimeField()
    LOG_TD = models.DateTimeField()
    NET_PAY = models.DateTimeField()
    OPERATOR =  models.CharField(max_length=200)
    PLOT_NAME  = models.CharField(max_length=200)
    PLUGBACK_DEPTH  = models.DateTimeField()
    R_WELL_PROFILE_ID = models.ForeignKey(R_WELL_STATUS, on_delete=models.CASCADE)
    #/WELL_PROFILE = models.ForeignKey(R_WELL_STATUS, on_delete=models.CASCADE)
    WATER_ACOUSTIC_VEL =  models.DateTimeField()
    WATER_DEPTH =  models.FloatField()
    WATER_DEPTH_DATUM =  models.CharField(max_length=200)
    IS_VIRTUAL = models.BooleanField()
    R_DATA_ACCESS_CATEGORY_ID = models.ForeignKey(R_DATA_ACCESS_CATEGORY,on_delete=models.CASCADE)







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


class HIERARCHY (models.Model):
    HIERARCHY_ID = models.AutoField(primary_key=True)
    HIERARCHY_NAME = models.CharField(max_length=200)


class HIERARCHY_DESC (models.Model):
    HIERARCHY_DESC_ID = models.AutoField(primary_key= True)

class HIERARCHY_LEVEL(models.Model):
    HIERARCHY_LEVEL_ID = models.BigAutoField(primary_key=True)
    HIERARCHY_DESC_ID= models.ForeignKey(HIERARCHY_DESC,on_delete=models.CASCADE)
    ORG_UNIT_ID = models.ForeignKey(ORG_UNIT,on_delete=models.CASCADE)
    PAREINT_HIERARCHY_LEVEL_ID = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='PARENT_WELLBORE_ID')
    FFECTIVE_DATE=models.DateTimeField()
    EXPIRED_DATE = models.DateTimeField()
    REAMRK = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)



 # ////////////////////////
 # Wellbore Class

 # ELLBORE: A Wellbore is a path of drilled footage, 
 # from Well Origin (top/start) to a terminating point (bottom/end).
 # //////////////////////

class WELLBORE(models.Model):
    WELLBORE_ID=models.BigAutoField(primary_key=True)
    WELL_ID = models.ForeignKey(WELL,on_delete=models.CASCADE)
    WELL_UWI = models.CharField(max_length=200) 
    WELLBORE_UWL = models.CharField(max_length=200) # //// WELLBORE UNIQUE IDENTIFIER: A unique name, code or number designated to the wellbore
    WELLBORE_NAME = models.CharField(max_length=200)
    WELLBORE_NUMBER = models.CharField(max_length=200)
    X_COORDINATE = models.DecimalField(max_digits=18, decimal_places=2)
    Y_COORNODATE = models.DecimalField(max_digits=18, decimal_places=2)
    CRS_ID = models.ForeignKey(CARTOREFERENCESYSTEM, on_delete=models.CASCADE)
    CRS_NAME = models.CharField()
    BH_X_COORDINATE = models.DecimalField(max_digits=18, decimal_places=2) #///. X/Y of bottom, which can hold a geographical latitude/longitude or projected X/Y depending on the value of CRS, which can be either a projected CRS or geographical datum.
    BH_Y_COORDINATE =models.DecimalField(max_digits=18, decimal_places=2) # /// X/Y of bottom, which can hold a geographical latitude/longitude or projected X/Y depending on the value of CRS, which can be either a projected CRS or geographical datum.
    BH_CRS_ID = models.IntegerField()
    BH_CRS_NAMR = models.CharField(max_length=200)
    FIELD_ID = models.ForeignKey(FIELD, on_delete=models.CASCADE)
    KB_ELEV= models.IntegerField #  /// KELLY BUSHING ELEVATION: The elevation of the kelly bushing (generally measured from sea level).
    GROUND_ELEV = models.IntegerField()  # /// GROUND ELEVEVATION: The elevation of the ground level.
    DERRICK_FLOOR_ELEV = models.DecimalField(max_length=5,decimal_places=2,max_digits=10) # /// DERRICK FLOOR ELEVATION: Elevations that are reported from the Derrick floor.
    DEPTH_DATUM_ID = models.ForeignKey(R_WELL_DATUM_TYPE,on_delete=models.CASCADE)
    DAPTH_DATUM  = models.CharField(max_length=200)
    DEPTH_DATUM_ELEV =  models.IntegerField()
    SPUD_DATE = models.DateTimeField(verbose_name="")  # /// SPUD DATE: Date the drilling operations commenced on the well. The first day hole is made.
    SPUD_DATE_TZ =  models.CharField(max_length=50)
    R_TIMEZONE_ID = models.ForeignKey(R_TIMEZONE,on_delete=models.CASCADE)
    COMPLETION_DATE = models.DateTimeField() # // COMPLETION DATE: Date on the official filing or completion report indicating the wellbore is established as ready to produce, inject or abandon.
    DRILL_TD = models.IntegerField() # /// DRILLERS TOTAL DEPTH: Total or maximum depth of the wellbore as reported by the operator/ driller.
    PLUGBACK_DEPTH = models.DecimalField(max_digits=18, decimal_places=2)
    KICK_OFF_DEPTH = models.DecimalField(max_digits=18, decimal_places=2)
    WATER_DEPTH = models.DecimalField(max_digits=18, decimal_places=2) # //// WATER DEPTH: Depth of the water at a well (measured from the water level to the mud line).
    PARENT_WELLBORE_ID = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    FORMATION_AT_TD = models.CharField(max_length=200)
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)





   
    


##    //////////////////////////////////////////////////////////////////////
#
#   class EQUIPMENT
#
#
# EQUIPMENT: Use this table to describe pieces of equipment that are real. 
# May be any kind of equipment, microscopes, gauges etc.

##    //////////////////////////////////////////////////////////////////////

class EQUIPMENT (models.Model):
    EQUIPMENT_ID = models.AutoField(primary_key=True)
    EQUIPMENT_NAME = models.CharField()
    COMMISSION_DATE = models.DateField()
    DECOMMISSION_DATE = models.DateField() 
  
    R_EQUIPMENT_SUB_TYPE_ID = models.ForeignKey(R_EQUIPMENT_SUB_TYPE , on_delete=models.CASCADE)
    EQUIPMENT_ALIAS_NAME= models.CharField()
    SERIAL_NUM = models.CharField() 
    MANUFACTURER_BA_ID = models.ForeignKey(ORG_UNIT, on_delete=models.CASCADE)
    SHORTNAME = models.CharField()
    LONGNAME = models.CharField()
    ROW_CREATED_BY= models.CharField(max_length=200)
    ROW_CREATED_DATE=models.DateTimeField()
    ROW_CHANGED_DATE = models.DateTimeField()
    ROW_CHANEGED_BY= models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)



    ## ##################### ##
    ##. class Pool 
    ## POOL/RESERVOIR: Represents a reservoir or a group of small tracts of land brought together for the granting of a well permit under applicable spacing rules.
    ##  In Canada pool almost exclusively refers to a reservoir and these codes are usually unique within a province/field. 
    ## In the United States, these codes are unique either to the state, 
    ## or to the state/field or the district. Pool definitions may be administrative (usually assigned to a production string) or geologic (usually assigned to a production string formation).
    ## #################### ##


class POOL_TYPE(models.Model):
    POOL_TYPE_ID = models.BigAutoField(primary_key=True)
    POOL_TYPE_NAME = models.CharField(max_length=200)
    IS_ACTIVE=models.BooleanField(default=True)
     
class POOL_STATUS(models.Model):
    POOL_STATUS_ID = models.BigAutoField(primary_key=True)
    POOL_STATUS_NAME = models.CharField(max_length=200)
   
    ROW_CREATED_BY= models.CharField(max_length=200,blank=True, null=True)
    ROW_CREATED_DATE=models.DateTimeField(blank=True, null=True)
    ROW_CHANGED_DATE = models.DateTimeField(blank=True, null=True)
    ROW_CHANEGED_BY= models.CharField(max_length=200,blank=True, null=True)
    IS_ACTIVE=models.BooleanField(default=True)
    
class POOL(models.Model):
    POOL_ID = models.BigAutoField(primary_key=True)
    POOL_NAME = models.CharField(max_length=200,blank=True, null=True)
    POOL_CODE = models.CharField(max_length=200,blank=True, null=True)
    POOL_NAME_ABBERATION = models.CharField(max_length=200,blank=True, null=True)
    POOL_STATUS_FK= models.ForeignKey(POOL_STATUS, on_delete=models.CASCADE) 
    POOL_TYPE_FK = models.ForeignKey(POOL_TYPE,on_delete=models.CASCADE)
    ROW_CREATED_BY= models.CharField(max_length=200,blank=True, null=True)
    ROW_CREATED_DATE=models.DateTimeField(blank=True, null=True)
    ROW_CHANGED_DATE = models.DateTimeField(blank=True, null=True)
    ROW_CHANEGED_BY= models.CharField(max_length=200,blank=True, null=True)
    IS_ACTIVE=models.BooleanField(default=True)

 ## ##################### ##
    ##. class zone 
    ## ZONE: The ZONE table contains the name of a zone described in a field or reservoir. A zone may be a regular or irregular belt,
    #  layer, band, or strip of earth materials disposed horizontally, vertically, concentrically or otherwise, and characterized as 
    # distinct from surrounding parts by some particular property or content.
    ## #################### ##
class ZONE(models.Model):
    ZONE_ID = models.BigAutoField(primary_key=True)
    zone_name = models.CharField(max_length=200,blank=True, null=True)
    POOL_ID = models.ForeignKey(POOL,on_delete=models.CASCADE)
    IS_ACTIVE=models.BooleanField(default=True)


                
    

# ##################### ##
##. Formation zone 
## FORMATION: Represents a specific layer of reservoir rock through which fluids flow from a reservoir into a string of production tubing. 
# This table can be used to prorate production from a production string back to individual formations.
# ## #################### ##

class Formation(models.Model):
    FORMATION_ID = models.BigAutoField(primary_key=True)
    FORMATION_NAME =models.CharField(max_length=200,blank=True, null=True)
    IS_ACTIVE=models.BooleanField(default=True)
