from django.urls import path
from escola.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('curso/<int:curso_id>/', index, name='index_curso'),  # URL com um curso específico
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]