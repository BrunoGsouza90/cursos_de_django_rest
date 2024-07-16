from django.urls import path
from .views import CursoAPIView, AvaliacaoAPIView

'''
    Forma correta de inserir rotas para views de serialização.
'''
urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]