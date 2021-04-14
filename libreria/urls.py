from django.urls import path
from .views import LibroListCVB,AutoreDetailCVB
app_name='libreria'
urlpatterns = [
    path('', LibroListCVB.as_view(), name='lista_libri'),
    path('autore/<int:pk>/', AutoreDetailCVB.as_view(), name='profilo_autore')
    
]