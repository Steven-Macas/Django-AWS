from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import GalleryImageForm
from .models import GalleryImage
import json
from django.http import JsonResponse

def ajax(request):
    list = []
    list.append({'x' : 1, 'y': 3})
    list.append({'x' : 2, 'y': 4})
    return JsonResponse(list, safe = False)

def usajax(request):
    return render(request, 'paginaas/usaajax.html')

# Create your views here.
def index(request):
    return HttpResponse("<h1>¡Bienvenido!</h1>")

def prueba(request):
    return render(request, 'paginas/prueba.html')

def detalle(request, iddetalle):
    return HttpResponse( "detalle %s." % iddetalle)

def upload(request):
    form = GalleryImageForm()
    return render(request, 'paginas/upload.html', {"form": form})

def manage_upload(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save()
            return redirect('en_face:show_image', id=object.id)
    return redirect('en_face:prueba', id = object.id)

def show_image(request, id):
    print(id)
    object = GalleryImage.objects.get(id=id)
    return render(request, 'paginas/show_image.html', {'data': object})

def proccess_image(request):
    context = {
        'coordenadas': request.POST('coordenadas'),
        'image':request.POST('imagen')
    }
    return render(request, 'paginas/proccess_image.html', context)
