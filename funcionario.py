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
        messagebox.showinfo("Inserir", "Funcionário inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Funcionário encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do funcionário alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Funcionário deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def Funcionario():
    Tela_Funcionario = Tk()
    Tela_Funcionario.title("Tela Funcionário")
    Tela_Funcionario.geometry("500x700")
    
    # Campos de entrada


    idFuncionario = Label(Tela_Funcionario, text="Id do Funcionario", font="Arial 10 bold")
    idFuncionario.pack(pady=5)
    
    Text_Id_Funcionario = Entry(Tela_Funcionario, font="Arial 10")
    Text_Id_Funcionario.pack(padx=10, pady=10)

    nomeFunc = Label(Tela_Funcionario, text="Nome do Funcionario", font="Arial 10 bold")
    nomeFunc.pack(pady=5)

    Text_Nome_Funcionario = Entry(Tela_Funcionario, font="Arial 10")
    Text_Nome_Funcionario.pack(padx=10, pady=10)

    Cargo = Label(Tela_Funcionario, text="Cargo do Funcionario", font="Arial 10 bold")
    Cargo.pack(pady=5)

    Text_Cargo_Funcionario = Entry(Tela_Funcionario, font="Arial 10")
    Text_Cargo_Funcionario.pack(padx=10, pady=10)

    Cargo = Label(Tela_Funcionario, text="Endereço do Funcionario", font="Arial 10 bold")
    Cargo.pack(pady=5)

    Text_Endereco_Funcionario = Entry(Tela_Funcionario, font="Arial 10")
    Text_Endereco_Funcionario.pack(padx=10, pady=10)

    Cargo = Label(Tela_Funcionario, text="Contato do Funcionario", font="Arial 10 bold")
    Cargo.pack(pady=5)

    Text_Contato_Funcionario = Entry(Tela_Funcionario, font="Arial 10")
    Text_Contato_Funcionario.pack(padx=10, pady=10)

    campos = [Text_Id_Funcionario, Text_Nome_Funcionario, Text_Cargo_Funcionario, Text_Endereco_Funcionario, Text_Contato_Funcionario]

    # Botões
    BotaoInserir = Button(Tela_Funcionario, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_Funcionario, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_Funcionario, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_Funcionario, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_Funcionario.mainloop()


BotaoFuncionario = Button(Tela_Inicial, text="Funcionário", font="Arial", width=15, height=2, command=Funcionario)
BotaoFuncionario.pack(padx=10, pady=10)






Tela_Inicial.mainloop()