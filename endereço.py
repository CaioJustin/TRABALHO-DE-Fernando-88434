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
        messagebox.showinfo("Inserir", "Endereço inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Endereço encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do Endereço alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Endereço deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def Endereco():
    Tela_Endereco = Tk()
    Tela_Endereco.title("Tela Endereço")
    Tela_Endereco.geometry("500x900")
    
    # Campos de entrada


    idEndereco = Label(Tela_Endereco, text="Id do Endereço", font="Arial 10 bold")
    idEndereco.pack(pady=5)

    Text_Id_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_Id_Endereco.pack(padx=4, pady=4)

    LogradouroEndereco = Label(Tela_Endereco, text="Logradouro", font="Arial 10 bold")
    LogradouroEndereco.pack(pady=4)

    Text_Logradouro_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_Logradouro_Endereco.pack(padx=4, pady=4)


    NumeroEndereco = Label(Tela_Endereco, text="numero endereço", font="Arial 10 bold")
    NumeroEndereco.pack(pady=5)

    Text_numero_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_numero_Endereco.pack(padx=4, pady=4)


    BairroEndereco = Label(Tela_Endereco, text="endereço do Bairro", font="Arial 10 bold")
    BairroEndereco.pack(pady=5)

    Text_bairro_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_bairro_Endereco.pack(padx=4, pady=4)   


    CidadeEndereco = Label(Tela_Endereco, text="Endereço da Cidade", font="Arial 10 bold")
    CidadeEndereco.pack(pady=5)

    Text_Cidade_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_Cidade_Endereco.pack(padx=4, pady=4)   


    UfEndereco = Label(Tela_Endereco, text="Uf Endereço", font="Arial 10 bold")
    UfEndereco.pack(pady=5)

    Text_Uf_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_Uf_Endereco.pack(padx=4, pady=4)  


    cepEndereco = Label(Tela_Endereco, text="Cep Endereço", font="Arial 10 bold")
    cepEndereco.pack(pady=5)

    Text_cep_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_cep_Endereco.pack(padx=4, pady=4)  


    ComplemtenEndereco = Label(Tela_Endereco, text="Complemento Endereço", font="Arial 10 bold")
    ComplemtenEndereco.pack(pady=5)

    Text_complemento_Endereco= Entry(Tela_Endereco, font="Arial 10")
    Text_complemento_Endereco.pack(padx=4, pady=4)  


    campos = [Text_Id_Endereco,Text_Logradouro_Endereco,Text_numero_Endereco,Text_bairro_Endereco,Text_Cidade_Endereco,Text_Uf_Endereco,Text_cep_Endereco,Text_complemento_Endereco]

    # Botões
    BotaoInserir = Button(Tela_Endereco, text="Inserir", font="Arial", width=15, height=2, command=lambda: inserir(campos))
    BotaoInserir.pack(padx=10, pady=10)

    BotaoPesq = Button(Tela_Endereco, text="Pesquisar", font="Arial", width=15, height=2, command=lambda: pesquisar(campos))
    BotaoPesq.pack(padx=10, pady=10)

    BotaoAlter = Button(Tela_Endereco, text="Alterar", font="Arial", width=15, height=2, command=lambda: alterar(campos))
    BotaoAlter.pack(padx=10, pady=10)

    BotaoDelete = Button(Tela_Endereco, text="Deletar", font="Arial", width=15, height=2, command=lambda: deletar(campos))
    BotaoDelete.pack(padx=10, pady=10)

    Tela_Endereco.mainloop()


BotaoEndereco = Button(Tela_Inicial, text="Manutenção", font="Arial", width=15, height=2, command=Endereco)
BotaoEndereco.pack(padx=10, pady=10)






Tela_Inicial.mainloop()