from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProyectoForm
from .models import Proyecto
from django.contrib.auth.decorators import login_required

# Create your views here.
def portafolio(request):
    return render(request,"portafolio/portafolio.html")


@login_required
def proyectos(request):
    proyectos = Proyecto.objects.filter(user=request.user)

    return render(request, "proyecto/proyectos.html", {
        'proyectos': proyectos
    })
    
@login_required
def create_proyecto(request):

    if request.method == 'GET':
        return render(request, "proyecto/create_proyecto.html", {
            'form': ProyectoForm
        })
    else:
        try:
            form = ProyectoForm(request.POST)
            new_proyecto = form.save(commit=False)
            new_proyecto.user = request.user
            new_proyecto.save()
            return redirect('proyectos')
        except ValueError:
            return render(request, 'proyecto/create_proyecto.html', {
                'form': ProyectoForm,
                'error': "Please provide valid data"
            })
            
@login_required
def proyecto_detail(request, proyecto_id):
    if request.method == 'GET':
        proyecto = get_object_or_404(Proyecto, pk=proyecto_id, user=request.user)
        form = ProyectoForm(instance=proyecto)
        return render(request, 'proyecto/proyecto_detail.html', {
            'proyecto': proyecto,
            'form': form,
        })
    else:
        try:
            proyecto = get_object_or_404(Proyecto, pk=proyecto_id, user=request.user)
            form = ProyectoForm(request.POST, instance = proyecto)
            form.save()
            return redirect('proyectos')
        except ValueError:
            return render(request, 'proyecto/proyecto_detail.html', {
            'proyecto': proyecto,
            'form': form,
            'error': "Error updating proyecto",
        })
            
    
@login_required
def delete_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id, user=request.user)
    if request.method == "POST":
        proyecto.delete()
        return redirect('proyectos')