from django.contrib import admin
from authe.models import registermodel
# Register your models here.

class registeradmin(admin.ModelAdmin):
    list_display=['username','password','email','phone','dob','gender']

admin.site.register(registermodel,registeradmin)
