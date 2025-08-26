from django.contrib import admin
from .models import SaidaIscas

@admin.register(SaidaIscas)
class SaidaIscasAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'quantidade', 'data_saida', 'lote_de', 'lote_ate', 'data_criacao']
    list_filter = ['cliente', 'data_saida', 'data_criacao']
    search_fields = ['cliente__nome', 'lote_de', 'lote_ate', 'observacoes']
    date_hierarchy = 'data_saida'
    ordering = ['-data_saida']
    
    fieldsets = (
        ('Informações do Cliente', {
            'fields': ('cliente',)
        }),
        ('Detalhes da Saída', {
            'fields': ('quantidade', 'data_saida', 'lote_de', 'lote_ate')
        }),
        ('Observações', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['data_criacao', 'data_atualizacao']
