from django.contrib import admin
from .models import Client, Project
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "desc",)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "business_obj", "tech_details", "tags", "client",)


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)