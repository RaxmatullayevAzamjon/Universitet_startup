from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    list_display = ["id","ism","jins","yosh","daraja"]
    list_display_links = ["ism"]
    search_fields = ["ism"]
    search_help_text = "Ustozni ism bo'yicha qiring."

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ["id","nom","aktiv"]
    list_display_links = ["nom"]
    list_filter = ["aktiv"]
    search_fields = ["nom"]
    search_help_text = "Yo'nalish nomi bo'yicha qidiring."

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ["id","nom","asosiy"]
    list_display_links = ["nom"]
    list_filter = ["asosiy","yonalish__nom"]
    search_fields = ["nom"]
    search_help_text = "Fan nomi bo'yicha qidiring."

