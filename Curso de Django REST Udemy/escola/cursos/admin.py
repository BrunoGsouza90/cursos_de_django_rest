from django.contrib import admin
from .models import Curso, Avaliacao

'''
    Registro da tabela "Curso".
'''
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    '''
        Mencionamento das colunas da tabela "Curso", com as colunas
            herdadas da tabela abstrata "Base".
    '''
    list_display = ['titulo', 'url', 'criacao', 'atualizacao', 'ativo']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo']

    '''
        Como a tabela "Avaliação" tem um relacionamento com a tabela
            "Curso" se faz necessário fazer menção dos arquivos
            abstratos da tabela "Base" para não haver conflitos.
    '''
    def criacao(self, obj):
        return obj.criacao
    criacao.short_description = 'criacao'

    def atualizacao(self, obj):
        return obj.atualizacao
    atualizacao.short_description = 'atualizacao'

    def ativo(self, obj):
        return obj.ativo
    ativo.short_description = 'ativo'