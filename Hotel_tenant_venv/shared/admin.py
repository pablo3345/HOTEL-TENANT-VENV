

from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from shared.models import Client,  Domain

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('id', 'name', 'schema_name', 'last_name', 'first_name','business_name', 'dni', 'cantidad_habitacion', 'email', 'is_active' )






admin.site.register(Domain) 

