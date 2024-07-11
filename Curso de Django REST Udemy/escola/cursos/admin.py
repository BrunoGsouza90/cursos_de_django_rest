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
    list_display = ['get_titulo', 'get_url', 'get_criacao', 'get_atualizacao', 'get_ativo']

    '''
        Dando titulos mais amigáveis para as colunas das tabelas.
    '''
    def get_titulo(self, obj):
        return obj.titulo
    get_titulo.short_description = 'Título do Curso'

    def get_url(self, obj):
        return obj.url
    get_url.short_description = 'URL do Curso'

    def get_criacao(self, obj):
        return obj.criacao
    get_criacao.short_description = 'Data de Criação do Curso'

    def get_atualizacao(self, obj):
        return obj.atualizacao
    get_atualizacao.short_description = 'Última Atualização do Curso'

    def get_ativo(self, obj):
        return obj.ativo
    get_ativo.short_description = 'Curso Ativo'

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['get_nome', 'get_email', 'get_avaliacao', 'curso_titulo', 'curso_url', 'curso_criacao', 'curso_atualizacao', 'curso_ativo']
    
    '''
        Como a tabela "Avaliação" tem um relacionamento com a tabela
            "Curso" se faz necessário fazer menção dos arquivos
            abstratos da tabela "Base" para não haver conflitos.
    '''
    def curso_field(self, obj, field_name):
        if obj.curso:
            return getattr(obj.curso, field_name)
        return None

    def curso_titulo(self, obj):
        return self.curso_field(obj, 'titulo')
    curso_titulo.short_description = 'Título do Curso'

    def curso_url(self, obj):
        return self.curso_field(obj, 'url')
    curso_url.short_description = 'URL do Curso'

    def curso_criacao(self, obj):
        return self.curso_field(obj, 'criacao')
    curso_criacao.short_description = 'Data de Criação do Curso'

    def curso_atualizacao(self, obj):
        return self.curso_field(obj, 'atualizacao')
    curso_atualizacao.short_description = 'Última Atualização do Curso'

    def curso_ativo(self, obj):
        return self.curso_field(obj, 'ativo')
    curso_ativo.short_description = 'Curso Ativo'

    '''
        Dando títulos mais amigáveis para as colunas da tabela 
            específica.
    '''
    def get_nome(self, obj):
        return obj.nome
    get_nome.short_description = 'Nome do Avaliador'

    def get_email(self, obj):
        return obj.email
    get_email.short_description = 'E-mail do Avaliador'

    def get_avaliacao(self, obj):
        return obj.avaliacao
    get_avaliacao.short_description = 'Nota do Avaliador'