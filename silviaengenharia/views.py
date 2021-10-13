from django.shortcuts import render, redirect
from .models import PaginaCliente, Email, FormCliente, Cliente, MensagemParaTodos
from . import emails
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def index(request, id=1):
    form = FormCliente()
    pagina = PaginaCliente.objects.get(id = id)
    return render(request, 'index.html', {
        'Pagina': pagina,
        'form': form
    }
)

def agradecimento(request):
    form = FormCliente(request.POST)
    email = Email.objects.get()
    emails.envia_email(
        email_cliente=request.POST['email'],
        login=email.login,
        senha=email.senha,
        assunto=email.assunto,
        mensagem=email.mensagem
    )
    if form.is_valid():
        form.save()
    return render(request, 'agradecimento.html')

def login(request):
    if request.method != "POST":
        return render(request, 'login.html')

    login = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=login, password=senha)
    if not user:
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        return redirect('email_clientes')

@login_required(redirect_field_name='login')
def email_clientes(request):
    if request.method != "POST":
        return render(request, 'email_clientes.html')

    email = Email.objects.get()
    clientes = Cliente.objects.all()
    assunto = request.POST.get('assunto')
    men = MensagemParaTodos.objects.get()
    if men == '' or assunto == '':
        messages.add_message(request, messages.ERROR, 'Nenhum dos campos pode estar vazio')
        return render(request, 'email_clientes.html')
    for cliente in clientes:
        try:
            emails.envia_email(
                email_cliente=cliente.email,
                login=email.login,
                senha=email.senha,
                assunto=assunto,
                mensagem=men.mensagem
            )
        except:
            pass
    messages.add_message(request, messages.SUCCESS, 'Emails enviados com sucesso!')
    return render(request, 'email_clientes.html', )