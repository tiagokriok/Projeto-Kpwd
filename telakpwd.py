import random
import tkinter as tk
from tkinter import BOTH, END
from tkinter import Frame
from tkinter import ttk


class kpwd(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.principal()

    def principal(self):
        # Título
        self.master.title('KPWD')

        self.pack(fill=BOTH, expand=1)
        # Label Caracteres
        lb_carac = ttk.Label(self, text='Digite o tamanho que a senha deve ter:')
        lb_carac.place(x=10, y=10)
        # Entrada Caracteres
        ent_carac = ttk.Entry(self, width=3, validate="key",
                              validatecommand=(self.register(self.ent_num), '%S'))
        ent_carac.place(x=220, y=10)
        # Retorno da senha
        tex_pass = tk.Text(self, bd=5, width=48, height=5)
        tex_pass.place(x=0, y=40)
        # Botão Gerar senha
        bt_ger = ttk.Button(self, text='Gerar Senha',
                            command=lambda: self.gerar_senha(ent_carac, tex_pass))
        bt_ger.place(x=170, y=150)

    def gerar_senha(self, carac, tex_pwd):
        tex_pwd.delete(1.0, END)
        num_carac = int(carac.get())
        carac = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        senha = ''
        for i in range(0, int(num_carac)):
            senha += carac[random.randint(0, len(carac) - 1)]
        tex_pwd.insert(1.0, senha)

    def ent_num(self, tecla):
        val = '1234567890'
        return tecla in val


telakpwd = tk.Tk()
telakpwd.geometry('400x200')
telakpwd.resizable(False, False)
app = kpwd(telakpwd)
telakpwd.mainloop()
