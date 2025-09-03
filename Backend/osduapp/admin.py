from django.contrib import admin

# Register your models here.
from .models import WELL,WELLBORE

# from .models import shoretype
# from .models import NIOC_Production_type
# from .models import NIOC_Production
 
admin.site.register(WELL)
admin.site.register(WELLBORE)
# admin.site.register(NIOC_Production_type)
# admin.site.register(NIOC_Production)