from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


# ==================== API V2 ====================

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get', 'post', 'put', 'delete', 'patch'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        
        if request.method == 'GET':
            serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = AvaliacaoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(curso=curso)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
        elif request.method in ['PUT', 'PATCH']:
            avaliacao_id = request.data.get('id')
            avaliacao = curso.avaliacoes.get(id=avaliacao_id)
            serializer = AvaliacaoSerializer(avaliacao, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        
        elif request.method == 'DELETE':
            avaliacao_id = request.data.get('id')
            avaliacao = curso.avaliacoes.get(id=avaliacao_id)
            avaliacao.delete()
            return Response(status=204)

# VIEWSET PADRÃO:
# Todos os métodos HTTP já vem includos.

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer



#   VIEWSET CUSTOMIZADA:
#   Implementamos os métodos HTTP específicos. 
'''
class AvaliacaoViewSet(mixins.CreateModelMixin, 
                       mixins.UpdateModelMixin, 
                       mixins.DestroyModelMixin, 
                       viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''