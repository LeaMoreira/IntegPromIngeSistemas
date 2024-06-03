import json
import tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

rutaLogin = "C:/Users/rokha/Desktop/material de estudio ucp/tercer año/programacion/1er cuatrimentre/inteProg/usuarios.json"
with open (rutaLogin, "r") as archivo:
    usuarios = json.load(archivo)

rutaStock = "C:/Users/rokha/Desktop/material de estudio ucp/tercer año/programacion/1er cuatrimentre/inteProg/productosInteg.json"
with open (rutaStock, "r") as archivo:
    stock = json.load(archivo)

def fn_soloLetras(input):
    return input.isalpha()

def fn_soloNumeros(input):
    return input.isdigit()


ventanaAñadirProducto = Tk()
ventanaAñadirProducto.title("Añadir Producto")

cuadroCombobox = LabelFrame(ventanaAñadirProducto, text="Elección de Secciones: ")
cuadroCombobox.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

categoriaTexto = Label(cuadroCombobox, text="Categoría")
categoriaTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)
categoriaCombobox = ttk.Combobox(cuadroCombobox, values= list(stock.keys()))
categoriaCombobox.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

seccionTexto = Label(cuadroCombobox, text="Seccion")
seccionTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)
seccionCombobox = ttk.Combobox(cuadroCombobox)
seccionCombobox.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

ventanaAñadirProducto.mainloop()