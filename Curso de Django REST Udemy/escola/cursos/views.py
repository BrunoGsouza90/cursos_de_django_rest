from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import status

'''
    Criação da View Curso que é aonde recebemos a requisição HTTP
        e enviamos uma resposta HTTP.
'''
class CursoAPIView(APIView):
    # Titulo que apareça no site emcima da API.
    '''
        API de Cursos da Geek University.
    '''

    '''
        Criação da função para visualização dos dados (GET).
        request = Aonde é armazenado todos os dados da requisição.
    '''
    def get(self, request):
        
        '''
            Verificando no terminal o que temos dentro de request.   

            Verificamos que não tem nada dentro de request, pois
                a requisição está pedindo dados, não está enviando
                dados.
            Por isso o dicionário vazio.   
        '''
        print(request.data)

        '''
            Verificamos aqui quem é o usuário que está consumindo
                a API.
            Se estivermos deslogados veremos que o usuário é um
                usuário sem autorização por isso está descrito como
                "AnonymousUser".
        '''
        print(request.user)
        print(request.user.id)

        '''
            Aqui vemos que se estivermos offline dará erros pq o email
                não é permitido ser acessado como espeficado no
                serializers.py caso o usuario esteja deslogado.

            "serialiazers.py" linha 47-49.
                extra_kwargs = {
                    'email': {'write_only': True}
                }

        '''
        #print(request.user.email)

        '''
        Importação de todos as colunas da tabela Cursos.
        '''
        cursos = Curso.objects.all()

        '''
            Aqui especificamos se vamos passar uma ou mais colunas,
                como vamos passar mais de uma colocamos alêm do
                parâmetro "cursos" o parâmetro "many=True", pois são
                muitos.
        '''
        serializer = CursoSerializer(cursos, many=True)

        '''
            Enviando a resposta HTTP em formato JSON.
        '''
        return Response(serializer.data)

    '''
        Criação da função para criação dos dados (POST).
        request = Aonde é armazenado todos os dados da requisição.
        Note que ao estar online o formulário só aparecerá se ele
            estiver logado, assim como definimos em settings.py.
    '''
    def post(self, request):

        '''
            Criação da variável que receberá os dados cujo serão
                enviados pela API como resposta.
        '''
        serializer = CursoSerializer(data=request.data)

        '''
            Verificando se os dados são válidos.
            raise_exception=True = Caso os dados não sejam válidos, será
                enviado de volta uma excessão e paramos a função aqui.
        '''
        serializer.is_valid(raise_exception=True)
        
        '''
            Caso os dados sejam válidos, os dados serão salvos.
        '''
        serializer.save()

        '''
            Retornando os dados em formato JSON e retornando uma resposta
                de sucesso de criação.
        '''
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AvaliacaoAPIView(APIView):
    '''
        API de Avaliações da Geek University.
    ''' 
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)