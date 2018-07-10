from django.shortcuts import render


# Create your views here.

def index(request):
    context = { 'nome': 'Luis Felipe' }
    return render(request, 'show/index.html', context)