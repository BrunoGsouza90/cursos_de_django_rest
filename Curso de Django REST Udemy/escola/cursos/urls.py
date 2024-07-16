'''
    Importação da biblioteca do Django Framework que retrata sobre rotas.
'''
from django.urls import path

'''
    Importação da biblioteca do Django Framework que fará menção as views
        que são a parte Django Framework responsável pelas requisões e
        repostas HTTP.
'''
from .views import CursosAPIView, CursoAPIView, AvaliacoesAPIView, AvaliacaoAPIView

'''
    Forma correta de inserir rotas para views de serialização.
'''
urlpatterns = [
    # Rotas genéricas para listagem completas do módulo, método GET e POST.
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    

    # Rotas genéricas para listagens únicas dos dados, indetificadas a partir
    #   dos Identificadores Primários no Banco de Dados (Primary Key).
    # Aqui também trateremos o método PUT e DELETE em views.py .
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]