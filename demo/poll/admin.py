from django.contrib import admin
#from demo.poll.models import *
from .models import *


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)

# Register your models here.
