from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
from apps.inscripcion.forms import horarioForm, loginForm
from django.contrib.auth.decorators import login_required


@login_required()
def horario(request):
    if request.method == 'POST':
        form = horarioForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('goEnviado')
    else:
        form = horarioForm()
    return render(request, 'home.html/', {'form': form})

def Enviado(request):
    return render(request,'enviado.html/')


