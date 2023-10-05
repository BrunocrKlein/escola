from django.shortcuts import render, get_object_or_404, redirect
from escola.models import Aluno, Curso, Matricula
from django.contrib import messages

def index(request, curso_id=None):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    cursos = Curso.objects.all()
    if curso_id is not None:
        matriculas = Matricula.objects.filter(curso_id=curso_id)  # Recupere as matrículas relacionadas a este curso
        alunos = [matricula.aluno for matricula in matriculas]
        return render(request, 'escola/index.html', {"cards": alunos, "cursos": cursos})
    else:
       alunos = Aluno.objects.all()
       return render(request, 'escola/index.html', {"cards": alunos, "cursos": cursos})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Aluno, pk=foto_id)
    return render(request, 'escola/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Aluno.objects.order_by("data_fotografia").filter(ativo=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "escola/buscar.html", {"cards": fotografias})