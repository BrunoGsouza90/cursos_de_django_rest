from django.urls import path, include
from .views import AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter
from .views import AvaliacaoViewSet, CursoViewSet

router = SimpleRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]