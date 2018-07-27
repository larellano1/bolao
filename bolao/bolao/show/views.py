from django.shortcuts import render
from .forms import ConvidarAmigo, BolaoForm

# Create your views here.

def index(request):
    context = {}
    return render(request, 'show/index.html', context)

def convidarAmigo(request):

    if request.user.is_authenticated:

        context = { "mensagem" : "Convite enviado. Obrigado!",
                "style" : "w3-pale-green"
             }

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ConvidarAmigo(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return render(request,'show/mensagem.html/', context)

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ConvidarAmigo()

        return render(request, 'show/convite.html', {'form': form})

    else:
        context = {
            "mensagem" : "Faça o login antes de continuar.",
            "style" : "w3-pale-red"
        }
        return render(request,'show/mensagem.html', context)

def criarBolao(request):

    if request.user.is_authenticated:

        context = { "mensagem" : "Bolão criado. Obrigado!",
                "style" : "w3-pale-green"
             }

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = BolaoForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return render(request,'show/mensagem.html/', context)

        # if a GET (or any other method) we'll create a blank form
        else:
            form = BolaoForm()

        return render(request, 'show/criarbolao.html', {'form': form})

    else:
        context = {
            "mensagem" : "Faça o login antes de continuar.",
            "style" : "w3-pale-red"
        }
        return render(request,'show/mensagem.html', context)