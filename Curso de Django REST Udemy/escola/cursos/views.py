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

class AvaliacaoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer