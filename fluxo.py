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
        messagebox.showinfo("Inserir", "Fluxo inserido no banco de dados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def pesquisar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Pesquisar", "Fluxo encontrado no banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def alterar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Alterar", "Dados do Fluxo alterados com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

def deletar(campos):
    if verificar_campos(campos):
        messagebox.showinfo("Deletar", "Fluxo deletado do banco de dados!")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


def Fluxo():
    Tela_Fluxo = Tk()
    Tela_Fluxo.title("Tela fluxo")
    Tela_Fluxo.geometry("500x900")
    
    # Campos de entrada


    idFluxo = Label(Tela_Fluxo, text="Id do Fluxo", font="Arial 10 bold")
    idFluxo.pack(pady=5)

    Text_Id_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_Id_Fluxo.pack(padx=4, pady=4)

    HoraSaidaFluxo = Label(Tela_Fluxo, text="Hora da Saida", font="Arial 10 bold")
    HoraSaidaFluxo.pack(pady=4)

    Text_HoraSaida_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_HoraSaida_Fluxo.pack(padx=4, pady=4)


    HoraRetornoFluxo = Label(Tela_Fluxo, text="hora do retorno", font="Arial 10 bold")
    HoraRetornoFluxo.pack(pady=5)

    Text_HoraRetorno_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_HoraRetorno_Fluxo.pack(padx=4, pady=4)


    DataretornoFluxo = Label(Tela_Fluxo, text="Data do retorno Fluxo", font="Arial 10 bold")
    DataretornoFluxo.pack(pady=5)

    Text_dataretorno_fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_dataretorno_fluxo.pack(padx=4, pady=4)   


    datasaidafluxo = Label(Tela_Fluxo, text="data da saida", font="Arial 10 bold")
    datasaidafluxo.pack(pady=5)

    Text_datasaida_fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_datasaida_fluxo.pack(padx=4, pady=4)   


    KmEstimado = Label(Tela_Fluxo, text="Km Estimado", font="Arial 10 bold")
    KmEstimado.pack(pady=5)

    Text_kmEstimado_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_kmEstimado_Fluxo.pack(padx=4, pady=4)  


    kmsaida = Label(Tela_Fluxo, text="km saida", font="Arial 10 bold")
    kmsaida.pack(pady=5)

    Text_kmsaida_fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_kmsaida_fluxo.pack(padx=4, pady=4)  


    kmEntrada = Label(Tela_Fluxo, text="Km Entrada", font="Arial 10 bold")
    kmEntrada.pack(pady=5)

    Text_kmEntrada_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_kmEntrada_Fluxo.pack(padx=4, pady=4)  


    kmPercorrido = Label(Tela_Fluxo, text="KM Percorrido", font="Arial 10 bold")
    kmPercorrido.pack(pady=5)

    Text_kmpercorrido_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_kmpercorrido_Fluxo.pack(padx=4, pady=4)  


    tempo_entrega = Label(Tela_Fluxo, text="tempo de entrega", font="Arial 10 bold")
    tempo_entrega.pack(pady=5)

    Text_TempoEntrega_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_TempoEntrega_Fluxo.pack(padx=4, pady=4) 


    alteracao = Label(Tela_Fluxo, text="Alteração", font="Arial 10 bold")
    alteracao.pack(pady=5)

    Text_Alteracao_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_Alteracao_Fluxo.pack(padx=4, pady=4) 


    caminhao = Label(Tela_Fluxo, text="id do Caminhão", font="Arial 10 bold")
    caminhao.pack(pady=5)

    Text_Caminhao_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_Caminhao_Fluxo.pack(padx=4, pady=4) 


    Funcionario = Label(Tela_Fluxo, text="id do Funcinario", font="Arial 10 bold")
    Funcionario.pack(pady=5)

    Text_funcionario_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_funcionario_Fluxo.pack(padx=4, pady=4) 

    Funcionario = Label(Tela_Fluxo, text="id do Funcinario", font="Arial 10 bold")
    Funcionario.pack(pady=5)

    Text_funcionario_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_funcionario_Fluxo.pack(padx=4, pady=4)


    cliente = Label(Tela_Fluxo, text="id do Cliente", font="Arial 10 bold")
    cliente.pack(pady=5)

    Text_Cliente_Fluxo= Entry(Tela_Fluxo, font="Arial 10")
    Text_Cliente_Fluxo.pack(padx=4, pady=4)


    campos = [Text_Id_Fluxo,Text_HoraSaida_Fluxo,Text_HoraRetorno_Fluxo,Text_dataretorno_fluxo,Text_datasaida_fluxo,Text_kmEstimado_Fluxo,Text_kmsaida_fluxo,Text_kmEntrada_Fluxo,Text_kmpercorrido_Fluxo,Text_TempoEntrega_Fluxo,Text_Alteracao_Fluxo,Text_Caminhao_Fluxo,Text_funcionario_Fluxo,Text_Cliente_Fluxo]

    # Botões
    BotaoInserir = Button(Tela_Fluxo, text="Inserir", font="Arial",  command=lambda: inserir(campos))
    BotaoInserir.pack()

    BotaoPesq = Button(Tela_Fluxo, text="Pesquisar", font="Arial",  command=lambda: pesquisar(campos))
    BotaoPesq.pack()

    BotaoAlter = Button(Tela_Fluxo, text="Alterar", font="Arial",  command=lambda: alterar(campos))
    BotaoAlter.pack()

    BotaoDelete = Button(Tela_Fluxo, text="Deletar", font="Arial",  command=lambda: deletar(campos))
    BotaoDelete.pack()

    Tela_Fluxo.mainloop()


BotaoFluxo = Button(Tela_Inicial, text="Fluxo", font="Arial", width=15, height=2, command=Fluxo)
BotaoFluxo.pack(padx=10, pady=10)






Tela_Inicial.mainloop()