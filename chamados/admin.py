from django.contrib import admin

from .models import Chamado


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "prioridade",
        "status",
        "solicitante",
        "tecnico",
        "criado_em",
    )
    list_filter = ("status", "prioridade", "tecnico")
    search_fields = ("titulo", "descricao")


# Register your models here.
