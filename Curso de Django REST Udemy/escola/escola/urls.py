from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Importação da Rota do Django REST Framework.
    path('auth/',include('rest_framework.urls')),
    path('api/v1/', include('cursos.urls')),
]
