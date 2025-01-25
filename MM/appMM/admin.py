from django.contrib import admin
from appMM.models import signuptable,Logintable,Carttable,Producttable,Billtable
# Register your models here.
admin.site.register(Logintable)
admin.site.register(signuptable)
admin.site.register(Carttable)
admin.site.register(Producttable)
admin.site.register(Billtable)