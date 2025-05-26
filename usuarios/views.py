from django.shortcuts import render, redirect, HttpResponse
from .models import Usuario
from hashlib import sha256


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

    
def validar_cadastro(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    nascimento = request.POST.get('nascimento')
    telefone = request.POST.get('telefone')
    senha = request.POST.get('senha')
    confirma_senha = request.POST.get('confirma_senha')

    if len(nome.strip()) == 0 or len(sobrenome.strip()) == 0 or len(email.strip()) == 0 or len(nascimento.strip()) == 0 or len(telefone.strip()) == 0 or len(senha.strip()) == 0 or len(confirma_senha.strip()) == 0: # Campos vazios
        return redirect('/auth/cadastro/?status=1') 
    
    usuario = Usuario.objects.filter(email=email).filter(telefone=telefone)
    if len(usuario) > 0: # e-mail ou telefone já está cadastrado
        return redirect('/auth/cadastro/?status=2')
    
    if senha != confirma_senha: # As senhas não coincidem.
        return redirect('/auth/cadastro/?status=3')
    
    if len(senha) < 8 or len(confirma_senha) < 8: # Senha menor que 8 digitos.
        return redirect('/auth/cadastro/?status=4')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            nascimento=nascimento,
            telefone=telefone,
            senha=senha

        )

        usuario.save()

        return redirect('/auth/cadastro/?status=0') # Tudo certo com o cadastro!
    
    except:
        return redirect('/auth/cadastro/?status=5')  # Ouve um erro no sistema!


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def esqueceu_senha(request):
    status = request.GET.get('status')
    return render(request, 'esqueceu_senha.html', {'status': status})


def validar_esqueceu_senha(request):
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email=email)

    if len(email.strip()) == 0:
        return redirect('/auth/esqueceu_senha/?status=1') # Campo do Email está vazio

    if len(usuario) == 0:
        return redirect('/auth/esqueceu_senha/?status=2') # Usuario não cadastrado
    
    else:
        try:
            return redirect('/auth/esqueceu_senha/?status=0') # Tudo certo
        
        except:
            return redirect('/auth/esqueceu_senha/?status=3') # Erro no sistema