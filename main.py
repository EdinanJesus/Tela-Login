from tkinter import*
from tkinter import Tk, ttk
from tkinter import messagebox

#Collors  
co0 = "#f0f3f5" #black
co1 = "#feffff" #white
co2 = "#3fb5a3" #green
co3 = "#38576b" #value
co4 = "#403d3d" #letters

#criando Janela
janela = Tk()
janela.title("")
janela.geometry('310x300')
janela.configure(background= co1)
janela.resizable(width=FALSE, height=FALSE)

#dividindo a janela

Frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
Frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW) 

Frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief="flat")
Frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW) 

#configurando o frame cima

l_nome = Label(Frame_cima, text="LOGIN", anchor=NE, font=("Ivy 25"),bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(Frame_cima, text="",width=275, anchor=NW, font=("Ivy 1"),bg=co2, fg=co4)
l_linha.place(x=10, y=45)

credenciais = ['Joao', '123456789']

# funcao verificar senha
def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('login', 'Seja Bem vindo Admin!!!')
    elif credenciais[0] == nome and credenciais[1]== senha:
        messagebox.showinfo('login', 'Seja Bem vindo de volta!!! ' +credenciais[0])
       #deletar itens dentro do frame 
        for widget in Frame_baixo.winfo_children():
            widget.destroy()

        for widget in Frame_cima.winfo_children():
            widget.destroy()
        
        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha')

# funcao apos verificacao

def nova_janela():
    l_nome = Label(Frame_cima, text="Usuario: "+credenciais[0], anchor=NE, font=("Ivy 25"),bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(Frame_cima, text="",width=275, anchor=NW, font=("Ivy 1"),bg=co2, fg=co4)
    l_linha.place(x=10, y=45)


    l_nome = Label(Frame_baixo, text="Seja Bem Vindo "+credenciais[0], anchor=NE, font=("Ivy 20"),bg=co1, fg=co4)
    l_nome.place(x=5, y=105)
#configurando o frame baixo

l_nome = Label(Frame_baixo, text="Nome *", anchor=NW, font=("Ivy 10"),bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(Frame_baixo, width=25, justify="left", font= ("",15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(Frame_baixo, text="Senha *", anchor=NW, font=("Ivy 10"),bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(Frame_baixo, width=25, justify="left",show='*', font= ("",15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(Frame_baixo, command=verificar_senha, text="ENTRAR",width=39, height=2, font=("Ivy 8 bold"),bg=co2, fg=co1, relief=GROOVE, overrelief=RIDGE)
b_confirmar.place(x=10, y=180)

janela.mainloop()