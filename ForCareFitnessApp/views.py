from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Usuario
from .models import Fichas  

def professor(request):
    return render(request, 'dashboards/professor.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def admin(request):
    return render(request, 'dashboards/admin.html')

def remover_fichas(request):
    # Verifique se há alguma ficha para remover
    if Fichas.objects.exists():
        # Obter a última ficha adicionada
        ultima_ficha = Fichas.objects.latest('id')  # Use 'id' para garantir que é a última ficha
        # Excluir a última ficha adicionada
        ultima_ficha.delete()

def adicionar_fichas(request):
    # Cria um novo objeto Fichas
    nova_ficha = Fichas()
    
    # Define os atributos da nova ficha conforme necessário
    # Por exemplo, se houver campos adicionais em Fichas, você os definiria aqui.
    # nova_ficha.campo1 = valor1
    # nova_ficha.campo2 = valor2
    # ...

    # Salva a nova ficha no banco de dados
    nova_ficha.save()

def fichas(request):
    # Conta a quantidade de objetos Fichas no banco de dados
    quantidade_fichas = Fichas.objects.count()
    return render(request, 'dashboards/fichas.html', {'quantidade_fichas': quantidade_fichas})


def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        nascimento = request.POST['nascimento']
        email = request.POST['email']
        cpf = request.POST['CPF']
        senha = request.POST['senha']
        
        usuario = Usuario(nome=nome, nascimento=nascimento, email=email, cpf=cpf, senha=senha)
        usuario.save()
        
        return redirect('login')  # Redirecionar para a página de login após o cadastro
    
    return render(request, 'usuarios/cadastro.html')

def login_view(request):
    if request.method == 'POST':
        email_or_cpf = request.POST['email']
        senha = request.POST['senha']
        
        # Verifica se o usuário existe com o email ou CPF fornecido e a senha correta
        try:
            usuario = Usuario.objects.get(email=email_or_cpf)
        except Usuario.DoesNotExist:
            try:
                usuario = Usuario.objects.get(cpf=email_or_cpf)
            except Usuario.DoesNotExist:
                # Se o usuário não existir, mostra mensagem de erro
                return render(request, 'usuarios/login.html', {'error_message': 'Usuário não encontrado.'})
        
        # Verifica se a senha está correta
        if usuario.senha == senha:
            # Se o login for feito com o email de administrador e a senha correta, redirecione para a view admin
            if email_or_cpf == 'administrador@gmail.com' and senha == '123':
                return redirect('admin')  # Redireciona para a view do administrador

                
            # Armazena o ID do usuário na sessão
            request.session['usuario_id'] = usuario.id
            # Redireciona para a página do aluno
            return redirect('aluno')
        else:
            # Se a senha estiver incorreta, mostra mensagem de erro
            return render(request, 'usuarios/login.html', {'error_message': 'Senha incorreta.'})
    
    # Se o método da requisição não for POST, renderiza a página de login
    return render(request, 'usuarios/login.html')

def aluno(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.get(id=usuario_id)
        return render(request, 'dashboards/aluno.html', {'usuario': usuario})
    return redirect('login')
