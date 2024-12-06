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
        messagebox.showinfo("Inserir", "Fornecedor inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Fornecedor encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do Fornecedor alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Fornecedor deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def fornecedor():
    Tela_fornecedor = Tk()
    Tela_fornecedor.title("Tela Fornecedor")
    Tela_fornecedor.geometry("500x900")
    
    # Campos de entrada


    idfornecedor = Label(Tela_fornecedor, text="Id do Fornecedor", font="Arial 10 bold")
    idfornecedor.pack(pady=5)

    Text_Id_fornecedor= Entry(Tela_fornecedor, font="Arial 10")
    Text_Id_fornecedor.pack(padx=4, pady=4)

    nomefornecedor = Label(Tela_fornecedor, text="nome do fornecedor", font="Arial 10 bold")
    nomefornecedor.pack(pady=4)

    Text_nome_fornecedor= Entry(Tela_fornecedor, font="Arial 10")
    Text_nome_fornecedor.pack(padx=4, pady=4)


    razaofornecedor = Label(Tela_fornecedor, text="razao do fornecedor", font="Arial 10 bold")
    razaofornecedor.pack(pady=5)

    Text_razao_fornecedor= Entry(Tela_fornecedor, font="Arial 10")
    Text_razao_fornecedor.pack(padx=4, pady=4)


    cnpjfornecedor = Label(Tela_fornecedor, text="Cnpj do Fornecedor", font="Arial 10 bold")
    cnpjfornecedor.pack(pady=5)

    Text_cnpj_fornecedor= Entry(Tela_fornecedor, font="Arial 10")
    Text_cnpj_fornecedor.pack(padx=4, pady=4)   


    enderecofornecedor = Label(Tela_fornecedor, text="endereço do Fornecedor", font="Arial 10 bold")
    enderecofornecedor.pack(pady=5)

    Text_endereco_fornecedor= Entry(Tela_fornecedor, font="Arial 10")
    Text_endereco_fornecedor.pack(padx=4, pady=4)  


    Contadofornecedor = Label(Tela_fornecedor, text="Contato do Fornecedor", font="Arial 10 bold")
    Contadofornecedor.pack(pady=5)

    Text_contato_fornecedor= Entry(Tela_fornecedor, font="Arial 10")
    Text_contato_fornecedor.pack(padx=4, pady=4)


    



    campos = [Text_Id_fornecedor,Text_nome_fornecedor,Text_razao_fornecedor,Text_cnpj_fornecedor,Text_endereco_fornecedor,Text_contato_fornecedor]

    # Botões
    BotaoInserir = Button(Tela_fornecedor, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_fornecedor, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_fornecedor, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_fornecedor, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_fornecedor.mainloop()


Botaofornecedor = Button(Tela_Inicial, text="Fornecedor", font="Arial", width=15, height=2, command=fornecedor)
Botaofornecedor.pack(padx=10, pady=10)






Tela_Inicial.mainloop()