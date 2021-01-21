from .models import Autore_lf,Libro_lf
from django.views.generic.detail import DetailView
from django.views.generic.list   import ListView
# Create your views here.


class AutoreDetailCVB(DetailView):
     model = Autore
     template_name = "autore.html"

class LibroListCVB(ListView):
     model = Libro
     template_name = "lista_libri.html"