from django.contrib import admin
from .models import fdetail,Exam,Department,f_sem,Building,Rooms,allotment,Strength,Available
# Register your models here.
admin.site.register(Exam)
admin.site.register(fdetail)
admin.site.register(Department)
admin.site.register(f_sem)
admin.site.register(Available)
admin.site.register(Rooms)
admin.site.register(Building)
admin.site.register(allotment)
admin.site.register(Strength)
