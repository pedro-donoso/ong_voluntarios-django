from django.contrib import admin

from .models import Voluntario, Evento

@admin.register(Voluntario)


class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'fecha_registro']
    search_fields = ['nombre', 'email']
    list_filter = ['fecha_registro']

@admin.register(Evento)


class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'fecha', 'get_voluntarios_count']
    filter_horizontal = ['voluntarios']
    list_filter = ['fecha']

    def get_voluntarios_count(self, obj):
        return obj.voluntarios.count()
    get_voluntarios_count.short_description = 'Voluntarios'
