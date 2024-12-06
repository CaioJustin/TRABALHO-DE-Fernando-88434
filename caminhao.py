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
        messagebox.showinfo("Inserir", "Caminhão inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Caminhão encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do Caminhão alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Caminhão deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def Caminhao():
    Tela_Caminhao = Tk()
    Tela_Caminhao.title("Tela Caminhao")
    Tela_Caminhao.geometry("500x900")
    
    # Campos de entrada


    idcaminhao = Label(Tela_Caminhao, text="Id do caminhao", font="Arial 10 bold")
    idcaminhao.pack(pady=5)

    Text_Id_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_Id_caminhao.pack(padx=4, pady=4)



    placacaminhao = Label(Tela_Caminhao, text="placa do caminhao", font="Arial 10 bold")
    placacaminhao.pack(pady=4)

    Text_placa_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_placa_caminhao.pack(padx=4, pady=4)


    marcacaminhao = Label(Tela_Caminhao, text="marca do caminhao", font="Arial 10 bold")
    marcacaminhao.pack(pady=5)

    Text_marca_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_marca_caminhao.pack(padx=4, pady=4)


    modelocaminhao = Label(Tela_Caminhao, text="modelo do caminhao", font="Arial 10 bold")
    modelocaminhao.pack(pady=5)

    Text_modelo_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_modelo_caminhao.pack(padx=4, pady=4)   


    corcaminhao = Label(Tela_Caminhao, text="cor do caminhao", font="Arial 10 bold")
    corcaminhao.pack(pady=5)

    Text_cor_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_cor_caminhao.pack(padx=4, pady=4)  


    tipocaminhao = Label(Tela_Caminhao, text="tipo do caminhao", font="Arial 10 bold")
    tipocaminhao.pack(pady=5)

    Text_tipo_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_tipo_caminhao.pack(padx=4, pady=4)


    capacidadecaminhao = Label(Tela_Caminhao, text="capacidade do caminhao", font="Arial 10 bold")
    capacidadecaminhao.pack(pady=5)

    Text_capacidade_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_capacidade_caminhao.pack(padx=4, pady=4)


    renavancaminhao = Label(Tela_Caminhao, text="renavan do caminhao", font="Arial 10 bold")
    renavancaminhao.pack(pady=5)

    Text_renavan_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_renavan_caminhao.pack(padx=4, pady=4)


    chassicaminhao = Label(Tela_Caminhao, text="chassi do caminhao", font="Arial 10 bold")
    chassicaminhao.pack(pady=5)

    Text_chassi_caminhao= Entry(Tela_Caminhao, font="Arial 10")
    Text_chassi_caminhao.pack(padx=4, pady=4)



    campos = [Text_Id_caminhao, Text_placa_caminhao, Text_marca_caminhao, Text_modelo_caminhao, Text_cor_caminhao,Text_tipo_caminhao,Text_capacidade_caminhao,Text_renavan_caminhao,Text_chassi_caminhao]

    # Botões
    BotaoInserir = Button(Tela_Caminhao, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_Caminhao, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_Caminhao, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_Caminhao, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_Caminhao.mainloop()


BotaoCaminhao = Button(Tela_Inicial, text="Caminhão", font="Arial", width=15, height=2, command=Caminhao)
BotaoCaminhao.pack(padx=10, pady=10)






Tela_Inicial.mainloop()