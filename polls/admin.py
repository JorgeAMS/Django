from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.


admin.site.register(Choice)
admin.site.register(Question)



