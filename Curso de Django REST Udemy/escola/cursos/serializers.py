from rest_framework import serializers
from . models import Curso, Avaliacao

'''
    Importação da Tabela "Avaliação para serialização que é onde os
        dados são convertidos para JSON.
'''
class AvaliacaoSerializer(serializers.ModelSerializer):

    '''
        Como a as colunas "criacao" e "ativo" são herdadas da tabela
            "Base" que é uma tabela abstrata e já está sendo usada pela
            tabela "Cursos" então precisamos herdar essas colunas
            diretamente de "Cursos", pois a tabela "Avaliação" tem
            um relacionamento com a tabela "Cursos". Fazemos isso
            para evitar conflitos.
    '''
    curso_criacao = serializers.DateTimeField(source='curso.criacao')
    curso_ativo = serializers.BooleanField(source='curso.ativo')

    class Meta:

        '''
            Tabela do Banco de Dados que está sendo serializada.
        '''
        model = Avaliacao

        '''
            Colunas da tabela do Banco de Dados que serão serializadas.
        '''
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'curso_criacao',
            'curso_ativo',
        )

        '''
            extra_kargs - write_only = Não permiti que o dado "email"
             quando a API for consumida seja lida (GET). A API quando
             solicitada poderá ser atualizada (PUT) ou criada (POST).
        '''
        extra_kwargs = {
            'email': {'write_only': True}
        }

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
        )
        