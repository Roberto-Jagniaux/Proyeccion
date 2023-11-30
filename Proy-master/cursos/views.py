from django.shortcuts import render
from .models import Cursos as CursoModel  # Cambia el alias del modelo
from django.core.paginator import Paginator

def cursos(request):
    cursos_u = CursoModel.objects.all()  # Usa el alias del modelo
    paginator = Paginator(cursos_u,2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "core/cursos.html", {'cursos_u': page_obj})

