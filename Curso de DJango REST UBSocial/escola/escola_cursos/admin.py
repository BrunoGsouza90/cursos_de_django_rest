from django.contrib import admin
from .models import Curso, Avaliacao

''' Modo de usar o Decorator, que é a configuração da
        tabela com o admin. '''
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    ''' Listagem das colunas da tabela que serao exibidas ao cadastrar
            um novo dado no Django Admin. '''
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')