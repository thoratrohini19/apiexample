from django.contrib import admin
from apiapp.models import Client, Project

class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'created_at', 'created_by']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'client_name', 'created_at', 'created_by_username']

    def client_name(self, obj):
        return obj.client.client_name

    def created_by_username(self, obj):
        return obj.created_by.username

# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
