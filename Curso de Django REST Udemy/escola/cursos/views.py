'''
    Importação da biblioteca de erro 404, onde será atuado quando um
        objeto for inexistente.
'''
from django.shortcuts import get_object_or_404

'''
    Importação da biblioteca Django REST Framework, que será responsabilizada
        por liberar classes genericas que facilitarão a criação das views.
'''
from rest_framework import generics

'''
    Importação da biblioteca de tabelas do Banco de Dados.
'''
from .models import Curso, Avaliacao

'''
    Importação da biblioteca responsável pelas serializações já feitas
        dos dados do Banco de Dados para JSON.
'''
from .serializers import CursoSerializer, AvaliacaoSerializer

'''
    Criação da função de criação da API relacionado a "Cursos".

    Aqui podemos utilizar o "ListCreateAPIView" que vai criar de maneira mais
        fácil as nossas requisições e repostas.
'''
class CursosAPIView(generics.ListCreateAPIView):

    '''
        Criação de uma variável recebendo todo o conteúdo da tabela "Curso"
            criada no Banco de Dados.
    '''
    queryset = Curso.objects.all()

    '''
        Criação de variável recebendo todos os os dados da tabela "Curso"
            do Banco de Dados já serializados para JSON.
    '''
    serializer_class = CursoSerializer

'''
    Aqui podemos utilizar o método GET para um só indivíduo e podemos fazer 
        o UPDATE e o DELETE.
'''
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer



class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    '''
        Criação de uma função irá sobrescrever todos os dados dessa
            tabela no Banco de Dados que tem um relacionamento com
            outra tabela em questão.
    '''
    def get_queryset(self):

        '''
            Aqui verificamos que se a avaliação tem algum relacionamento
                com algum registro da tabela cujo existe o relacionamento.
        '''
        if self.kwargs.get('curso_pk'):

            '''
                Caso tenha um registro se relacionando, o valor será
                    retornado.
            '''
            return self.queryset.filter(pk=self.kwargs.get('curso_pk'))
        
        '''
            Caso não tenha um registro se relacionando, todos os valores dessa
                tabela serão retornados.
        '''
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    '''
        Criação de uma função que irá sobrescrever um dado único desta tabela
            no Banco de Dados que tem um relacionamento com outra tabela
            em questão.
    '''
    def get_object(self):

        '''
            Aqui verificamos se a avaliação tem algum relacionamento
                com algum registro da tabela cujo existe o relacionamento.
        '''
        if self.kwargs.get('curso_pk'):

            '''
                Após pegar todos os cursos ( Linha 98 ), filtramos, tendo em
                    mente que o curso_id seja o curso_pk, que é o relacionado
                    a avaliação mencionada em questão no endpoint, e que está
                    avaliação seja a avaliação específica do endpoint.
                Caso não exista o erro 404 é mencionado. 
            '''
            return get_object_or_404(self.get_queryset(), 
                                     curso_id=self.kwargs.get('curso_pk'), 
                                     pk=self.kwargs.get('avaliacao_pk'))
    
        '''
            Caso não tenha um registro se relacionando, todos os valores
                dessa tabela serão retornados.
        '''
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))