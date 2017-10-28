from django.shortcuts import render

# Create your views here.

def cursos_list(request):
    return render(request, 'curso/cursos_list.html', {})
