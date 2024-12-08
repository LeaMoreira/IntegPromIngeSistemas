import json
import tkinter
import modADMAgregar


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modADMAgregar import listaStock

rutaLogin = "C:/Users/rokha/Desktop/inteProg/usuarios.json"
with open (rutaLogin, "r") as archivo:
    usuarios = json.load(archivo)

rutaStock = "C:/Users/rokha/Desktop/inteProg/productos.json"
with open (rutaStock, "r") as archivo:
    stock = json.load(archivo)



def fn_modModificar():

    def fn_soloNumeros(input):
        return input.isdigit()

    ventanaModificarProducto = Tk()
    ventanaModificarProducto.title("Ventana Modificación de Producto")

    validacion_numeros = ventanaModificarProducto.register(fn_soloNumeros)

    itemSeleccionado = listaStock.selection()
    nombreProductoSeleccionado = listaStock.item(itemSeleccionado, "values")[1]
    nombreProductoTexto = Label(ventanaModificarProducto, text=f"{nombreProductoSeleccionado}")
    nombreProductoTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand= True)

    ventanaModificarProducto.mainloop()