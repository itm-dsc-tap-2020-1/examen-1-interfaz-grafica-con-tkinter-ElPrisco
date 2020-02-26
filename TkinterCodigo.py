import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
contador = 0
ventana = tk.Tk()
ventana.geometry("800x700")
ventana.title("Examen de fisica")


def funcion_click():
    aux = opcion.get()
    aux2 = opcion2.get()
    if pregunta1.get() == 100:
        contador = contador + 1
    if pregunta2.get() == 1000:
        contador = contador + 1
    if aux == 3:
        contador = contador + 1
    if aux2 == 3:
        contador = contador + 1
    if var1.get() == 1 or var2.get() == 1:
        contador = contador + 1
    mBox.showinfo('Calificacion',contador + ' de 5')   




ttk.Label(ventana, text = "Pregunta 1.- Cuantos centimetros tiene un metro?").grid(column = 0, row = 0)
pregunta1 = tk.StringVar()
Ppregunta1 = ttk.Entry(ventana, width=20, textvariable=pregunta1).grid(column = 0, row = 1)

ttk.Label(ventana, text = "Pregunta 2.- Cuantos metros tiene un kilometro?").grid(column = 0, row = 2)
pregunta2 = tk.StringVar()
Ppregunta2 = ttk.Entry(ventana, width=20, textvariable=pregunta2).grid(column = 0, row = 3)

ttk.Label(ventana, text = "Pregunta 3.- Valor promedio de la gravedad").grid(column = 0, row = 4)
opcion = tk.IntVar()
radio1 = tk.Radiobutton(ventana, text= "6.20", variable= opcion, value=1)
radio1.grid(column=0,row=5)
radio2 = tk.Radiobutton(ventana, text= "7.12", variable= opcion, value=2)
radio2.grid(column=1,row=5)
radio3 = tk.Radiobutton(ventana, text= "9.81", variable= opcion, value=3)
radio3.grid(column=2,row=5)

ttk.Label(ventana, text = "Pregunta 4.- Cuantas leyes de newton hay?").grid(column = 0, row = 6)
opcion2 = tk.IntVar()
radio4 = tk.Radiobutton(ventana, text= "7", variable= opcion2, value=1)
radio4.grid(column=0,row=7)
radio5 = tk.Radiobutton(ventana, text= "8", variable= opcion2, value=2)
radio5.grid(column=1,row=7)
radio6 = tk.Radiobutton(ventana, text= "3", variable= opcion2, value=3)
radio6.grid(column=2,row=7)

ttk.Label(ventana, text = "Pregunta 5.- Aportadores a la fisica").grid(column = 0, row = 8)
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
chk = tk.Checkbutton(ventana, text="Einstein", variable=var1)
chk.grid(column=0, row=9)
chk2 = tk.Checkbutton(ventana, text="Michael Jordan", variable=var2)
chk2.grid(column=1,row=9)
chk3 = tk.Checkbutton(ventana, text="Newton", variable=var3)
chk3.grid(column=2,row=9)
chk4 = tk.Checkbutton(ventana, text="Elvis Presley", variable=var4)
chk4.grid(column=3,row=9)
chk5 = tk.Checkbutton(ventana, text="Homero Simpson", variable=var5)
chk5.grid(column=4,row=9)

accion = ttk.Button(ventana,text="Calificar", command = funcion_click)
accion.grid(column=1, row=10)
ventana.mainloop()