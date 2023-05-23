from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'Nordestina/home.html')

@login_required
def dashView(request):
    return render(request, 'Nordestina/dashView.html')

@login_required
def create(request):
    return render(request, 'Nordestina/create.html')

@login_required
def painel(request):
    return render(request, 'Nordestina/painel.html')

def logina(request):
    data = {}
    userView = 'view'
    passView = ''
    if (userView == request.POST['username'] and passView == request.POST['password']):
        return render(request, 'Nordestina/dashView.html')
    else: 
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'Nordestina/painel.html')
        else:
            data['msg'] =  'Senhas diferentes'
            data['class'] = 'alert-danger'
            return render(request, 'Nordestina/home.html')

def store(request):
    data = {}
    if (request.POST['password'] != request.POST['password_confirm']):
        data['msg'] =  'Senhas diferentes'
        data['class'] = 'alert-danger'

    elif User.objects.filter(username=request.POST['User']).exists():
            data['msg'] = 'Usuário já existe'
            data['class'] = 'alert-danger'

    else:
        user = User.objects.create_user(username=request.POST['User'], email=request.POST['email'], password=request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso'
        data['class'] = 'alert-success'
         
    return render(request, 'Nordestina/create.html', data)
