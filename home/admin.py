from django.contrib import admin
from .models import SmartPhones,Other,Music,HomeAppliances,Wearables,Contact
# Register your models here.

admin.site.register(SmartPhones)
admin.site.register(Music)
admin.site.register(Wearables)
admin.site.register(HomeAppliances)
admin.site.register(Other)
admin.site.register(Contact)
