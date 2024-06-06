from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html',{"itens": Roupa.objects.all()})

def inicio(request):
    return render(request, 'myapp/inicio.html',{"itens": Roupa.objects.all()})

def create(request):
    form = RoupaForm
    if request.method == "POST":
        form = RoupaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "myapp/create.html", {"forms":form})



def edit(request, id):
    item = Roupa.objects.get(pk=id)
    form = RoupaForm(instance=item)
    return render(request, "myapp/update.html",{"form":form, "item":item})


def update(request, id):
    try:
        if request.method == "POST":
            item = Roupa.objects.get(pk=id)
            form = RoupaForm(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    item = Roupa.objects.get(pk=id)
    return render(request, "myapp/read.html", {"item":item})

def delete(request, id):
    item = Roupa.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # Substitua 'home' pela URL desejada após o login
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'myapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home') # Substitua 'home' pela URL desejada após o cadastro
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'myapp/home.html')