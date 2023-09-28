from django.contrib import admin
from .models import *



# tables add to admin

admin.site.register(Movie)
admin.site.register(Images)
admin.site.register(Cast)