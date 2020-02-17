from django.contrib import admin
from apptourisme.models import Hotel
from apptourisme.models import Restaurant
from apptourisme.models import Contact
from apptourisme.models import VisitGuidee
from apptourisme.models import Guidee
from apptourisme.models import Activite
from apptourisme.models import Transport


# Register your models here.
admin.site.register(Hotel)
admin.site.register(Restaurant)
admin.site.register(Contact)
admin.site.register(VisitGuidee)
admin.site.register(Guidee)
admin.site.register(Activite)
admin.site.register(Transport)
