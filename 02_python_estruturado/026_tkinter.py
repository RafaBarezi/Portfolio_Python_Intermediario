from tkinter import *

janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Minha janela exibida")
texto.place(x=50, y=100)
texto.pack()


def funcClicar():
    print("Botão pressionado")


pic = PhotoImage(
    file="")
logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

botao = Button(master=janelaPrincipal, text='Clique', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()