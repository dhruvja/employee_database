from django.contrib import admin
from .models import Faculty, Conference, Journal
# Register your models here.

admin.site.register(Faculty)
admin.site.register(Conference)
admin.site.register(Journal)