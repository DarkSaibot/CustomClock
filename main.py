import tkinter as tk
from tkinter import *
import os
from time import strftime
import locale

locale.setlocale(locale.LC_TIME, "pt_BR")


root = tk.Tk()
root.title('Meu Relógio')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background = '#08074B')

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text= 'Olá, ' + nome_usuario )

def get_data():
    data_atual = strftime("%A %d, %B %Y")
    data.config(text= data_atual) 
    
def get_horario():
    hora_atual = strftime('%H:%M:%S')
    horario.config(text= hora_atual)
    horario.after(1000, get_horario)
    
margem =  tk.Canvas(root, width = 600, height= 60, bg='#08074B', bd= 0, highlightthickness= 0, relief= "ridge") 
margem.pack()   

saudacao = Label(root, bg = '#08074B', fg= '#00BF9C', font = ( 'Gotham', 17))
saudacao.pack()

data = Label(root, bg = '#08074B', fg= '#00BF9C', font = ( 'Gotham', 15))
data.pack(pady=2)

horario = Label(root, bg = '#08074B', fg= '#00BF9C', font = ( 'Gotham', 65))
horario.pack(pady=2)

    
get_horario()    
get_data()
get_saudacao()
root.mainloop()





