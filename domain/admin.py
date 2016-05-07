from django.contrib import admin
from domain.models import Rocker

@admin.register(Rocker)
class RockerAdmin(admin.ModelAdmin):
	pass