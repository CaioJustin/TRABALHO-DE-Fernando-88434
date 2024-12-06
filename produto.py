from tkinter import *
from tkinter import messagebox

"""
Componemtes da Equipe:

Caio Justino de jesus santos
Kaio sergio
Marcus Viniccius
Vinnicius Nascimento
"""



Tela_Inicial = Tk()
Tela_Inicial.title("Menu Inicial")
Tela_Inicial.geometry("500x300")


NomeProjeto = Label(Tela_Inicial, text="Projeto IOT", font="Arial 20 bold")
NomeProjeto.pack()



def verificar_campos(campos):
    for campo in campos:
        if not campo.get():
            return False
    return True

def inserir(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Inserir", "Produto inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Produto encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do Produto alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Produto deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def Produto():
    Tela_Produto = Tk()
    Tela_Produto.title("Tela Produto")
    Tela_Produto.geometry("500x900")
    
    # Campos de entrada


    idProduto = Label(Tela_Produto, text="Id do Produto", font="Arial 10 bold")
    idProduto.pack(pady=5)

    Text_Id_Produto= Entry(Tela_Produto, font="Arial 10")
    Text_Id_Produto.pack(padx=4, pady=4)

    tipoProduto = Label(Tela_Produto, text="Tipo do Produto", font="Arial 10 bold")
    tipoProduto.pack(pady=4)

    Text_tipo_Produto= Entry(Tela_Produto, font="Arial 10")
    Text_tipo_Produto.pack(padx=4, pady=4)


    validadeProduto = Label(Tela_Produto, text="Validade do Produto", font="Arial 10 bold")
    validadeProduto.pack(pady=5)

    Text_validade_Produto= Entry(Tela_Produto, font="Arial 10")
    Text_validade_Produto.pack(padx=4, pady=4)


    obsProduto = Label(Tela_Produto, text="obs do Produto", font="Arial 10 bold")
    obsProduto.pack(pady=5)

    Text_Obs_Produto= Entry(Tela_Produto, font="Arial 10")
    Text_Obs_Produto.pack(padx=4, pady=4)   


    nomeProduto = Label(Tela_Produto, text="nome do Produto", font="Arial 10 bold")
    nomeProduto.pack(pady=5)

    Text_nome_Produto= Entry(Tela_Produto, font="Arial 10")
    Text_nome_Produto.pack(padx=4, pady=4)   


    QuantidadeProduto = Label(Tela_Produto, text="Quantidade do Produto", font="Arial 10 bold")
    QuantidadeProduto.pack(pady=5)

    Text_Quantidade_Produto= Entry(Tela_Produto, font="Arial 10")
    Text_Quantidade_Produto.pack(padx=4, pady=4)  




    campos = [Text_Id_Produto,Text_tipo_Produto,Text_validade_Produto,Text_Obs_Produto,Text_nome_Produto,Text_Quantidade_Produto]

    # Botões
    BotaoInserir = Button(Tela_Produto, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_Produto, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_Produto, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_Produto, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_Produto.mainloop()


BotaoProduto = Button(Tela_Inicial, text="Produto", font="Arial", width=15, height=2, command=Produto)
BotaoProduto.pack(padx=10, pady=10)






Tela_Inicial.mainloop()