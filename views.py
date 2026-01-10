from django.http import HttpResponse
from django.shortcuts import render

from produto.models import Produto


# Create your views here.
def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco')

        produto = Produto(nome, descricao, quantidade, preco)
        return HttpResponse(
                            f"Cliente cadastrado com sucesso! <br>: "
                            f"<br> Nome: {produto.nome} "
                            f"<br> Descrição: {produto.descricao}"
                            f"<br> Quantidade: {produto.quantidade} "
                            f"<br> Preço: {produto.preco}"
         )
    return render(request, 'cadastro_produto.html')