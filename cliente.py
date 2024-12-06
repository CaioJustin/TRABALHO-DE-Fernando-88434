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
        messagebox.showinfo("Inserir", "Cliente inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Cliente encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do Cliente alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Cliente deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def Cliente():
    Tela_Cliente = Tk()
    Tela_Cliente.title("Tela Cliente")
    Tela_Cliente.geometry("500x900")
    
    # Campos de entrada


    idCliente = Label(Tela_Cliente, text="Id do Cliente", font="Arial 10 bold")
    idCliente.pack(pady=5)

    Text_Id_Cliente= Entry(Tela_Cliente, font="Arial 10")
    Text_Id_Cliente.pack(padx=4, pady=4)

    nomeCliente = Label(Tela_Cliente, text="nome do Cliente", font="Arial 10 bold")
    nomeCliente.pack(pady=4)

    Text_nome_Cliente= Entry(Tela_Cliente, font="Arial 10")
    Text_nome_Cliente.pack(padx=4, pady=4)


    cpfCliente = Label(Tela_Cliente, text="cpf do Cliente", font="Arial 10 bold")
    cpfCliente.pack(pady=5)

    Text_cpf_Cliente= Entry(Tela_Cliente, font="Arial 10")
    Text_cpf_Cliente.pack(padx=4, pady=4)


    cnpjCliente = Label(Tela_Cliente, text="cnpj do Cliente", font="Arial 10 bold")
    cnpjCliente.pack(pady=5)

    Text_cnpj_Cliente= Entry(Tela_Cliente, font="Arial 10")
    Text_cnpj_Cliente.pack(padx=4, pady=4)   


    enderecoCliente = Label(Tela_Cliente, text="Endereço do Cliente", font="Arial 10 bold")
    enderecoCliente.pack(pady=5)

    Text_endereco_Cliente= Entry(Tela_Cliente, font="Arial 10")
    Text_endereco_Cliente.pack(padx=4, pady=4)   


    ContatoCliente = Label(Tela_Cliente, text="Contato do Cliente", font="Arial 10 bold")
    ContatoCliente.pack(pady=5)

    Text_contato_Cliente= Entry(Tela_Cliente, font="Arial 10")
    Text_contato_Cliente.pack(padx=4, pady=4)  




    campos = [Text_Id_Cliente,Text_nome_Cliente,Text_cpf_Cliente,Text_cnpj_Cliente,Text_endereco_Cliente,Text_contato_Cliente]

    # Botões
    BotaoInserir = Button(Tela_Cliente, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_Cliente, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_Cliente, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_Cliente, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_Cliente.mainloop()


BotaoCliente = Button(Tela_Inicial, text="Cliente", font="Arial", width=15, height=2, command=Cliente)
BotaoCliente.pack(padx=10, pady=10)






Tela_Inicial.mainloop()