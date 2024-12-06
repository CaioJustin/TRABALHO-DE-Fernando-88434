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
        messagebox.showinfo("Inserir", "Contato inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Contato encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do Contato alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Contato deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def contato():
    Tela_contato = Tk()
    Tela_contato.title("Tela Contato")
    Tela_contato.geometry("500x900")
    
    # Campos de entrada


    idContato = Label(Tela_contato, text="Id do contato", font="Arial 10 bold")
    idContato.pack(pady=5)

    Text_Id_Contato= Entry(Tela_contato, font="Arial 10")
    Text_Id_Contato.pack(padx=4, pady=4)

    celularContato = Label(Tela_contato, text="celular do contato", font="Arial 10 bold")
    celularContato.pack(pady=4)

    Text_celular_Contato= Entry(Tela_contato, font="Arial 10")
    Text_celular_Contato.pack(padx=4, pady=4)


    telefoneContato = Label(Tela_contato, text="telefone do Contato", font="Arial 10 bold")
    telefoneContato.pack(pady=5)

    Text_telefone_Contato= Entry(Tela_contato, font="Arial 10")
    Text_telefone_Contato.pack(padx=4, pady=4)


    emailContato = Label(Tela_contato, text="email do Contato", font="Arial 10 bold")
    emailContato.pack(pady=5)

    Text_email_Contato= Entry(Tela_contato, font="Arial 10")
    Text_email_Contato.pack(padx=4, pady=4)   



    campos = [Text_Id_Contato,Text_celular_Contato,Text_telefone_Contato,Text_email_Contato]

    # Botões
    BotaoInserir = Button(Tela_contato, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_contato, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_contato, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_contato, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_contato.mainloop()


BotaoContato = Button(Tela_Inicial, text="contato", font="Arial", width=15, height=2, command=contato)
BotaoContato.pack(padx=10, pady=10)






Tela_Inicial.mainloop()