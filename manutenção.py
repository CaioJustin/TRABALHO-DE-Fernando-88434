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
        messagebox.showinfo("Inserir", "item em Manutenção inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "item em Manutenção encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do item em Manutenção alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "item em Manutenção deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def Manutencao():
    Tela_Manutencao = Tk()
    Tela_Manutencao.title("Tela Manutenção")
    Tela_Manutencao.geometry("500x900")
    
    # Campos de entrada


    idManutencao = Label(Tela_Manutencao, text="Id da Manutenção", font="Arial 10 bold")
    idManutencao.pack(pady=5)

    Text_Id_Manutencao= Entry(Tela_Manutencao, font="Arial 10")
    Text_Id_Manutencao.pack(padx=4, pady=4)

    dataentraManutencao = Label(Tela_Manutencao, text="data da entrada da Manutenção", font="Arial 10 bold")
    dataentraManutencao.pack(pady=4)

    Text_DataEntrada_Manutencao= Entry(Tela_Manutencao, font="Arial 10")
    Text_DataEntrada_Manutencao.pack(padx=4, pady=4)


    dataSaidaManutencao = Label(Tela_Manutencao, text="data de Saida da Manutenção", font="Arial 10 bold")
    dataSaidaManutencao.pack(pady=5)

    Text_DataSaida_Manutencao= Entry(Tela_Manutencao, font="Arial 10")
    Text_DataSaida_Manutencao.pack(padx=4, pady=4)


    descManutencao = Label(Tela_Manutencao, text="descrição da Manutenção", font="Arial 10 bold")
    descManutencao.pack(pady=5)

    Text_desc_Manutencao= Entry(Tela_Manutencao, font="Arial 10")
    Text_desc_Manutencao.pack(padx=4, pady=4)   


    CaminhaoManutencao = Label(Tela_Manutencao, text="Caminhao em Manutenção", font="Arial 10 bold")
    CaminhaoManutencao.pack(pady=5)

    Text_caminhao_Manutencao= Entry(Tela_Manutencao, font="Arial 10")
    Text_caminhao_Manutencao.pack(padx=4, pady=4)   


    FuncionarioManutencao = Label(Tela_Manutencao, text="Funcionario da Manutenção", font="Arial 10 bold")
    FuncionarioManutencao.pack(pady=5)

    Text_Funcionario_Manutencao= Entry(Tela_Manutencao, font="Arial 10")
    Text_Funcionario_Manutencao.pack(padx=4, pady=4)  


    pecaManutencao = Label(Tela_Manutencao, text="Peças da Manutenção", font="Arial 10 bold")
    pecaManutencao.pack(pady=5)

    Text_pecas_Manutencao= Entry(Tela_Manutencao, font="Arial 10")
    Text_pecas_Manutencao.pack(padx=4, pady=4)  




    campos = [Text_Id_Manutencao,Text_DataEntrada_Manutencao,Text_DataSaida_Manutencao,Text_desc_Manutencao,Text_caminhao_Manutencao,Text_Funcionario_Manutencao,Text_pecas_Manutencao]

    # Botões
    BotaoInserir = Button(Tela_Manutencao, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_Manutencao, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_Manutencao, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_Manutencao, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_Manutencao.mainloop()


BotaoManutencao = Button(Tela_Inicial, text="Manutenção", font="Arial", width=15, height=2, command=Manutencao)
BotaoManutencao.pack(padx=10, pady=10)






Tela_Inicial.mainloop()