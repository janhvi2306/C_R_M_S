from django.contrib import admin
from home.models import Register,Job_det,Apply_for_job,User,ShortlistedCand

# Register your models here.

admin.site.register(Register)
admin.site.register(Job_det)
admin.site.register(Apply_for_job)
admin.site.register(ShortlistedCand)



