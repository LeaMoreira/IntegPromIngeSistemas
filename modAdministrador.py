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

modAdmin_Ventana = Tk()
modAdmin_Ventana.title("Ventana Administrador")

ventanaBotones = LabelFrame(modAdmin_Ventana, text="Accesibilidades: ")
ventanaBotones.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

agregar_Boton = Button(ventanaBotones, text="Agregar Producto")
agregar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT)

modificar_Boton = Button(ventanaBotones, text="Modificar Producto")
modificar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT)

eliminar_Boton = Button(ventanaBotones, text="Eliminar Producto")
eliminar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT)

ventanaTreeview = LabelFrame(modAdmin_Ventana, text="Lista de Stock producto: ")
ventanaTreeview.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

listaStock = ttk.Treeview(ventanaTreeview, columns=("Categoria", "Producto", "ID Producto", "Cantidad", "Precio"))
listaStock.pack(ipadx= 200, ipady= 70, padx= 5, pady= 5, side= LEFT)
listaStock.heading("#0", text="Categoría")
listaStock.heading("#1", text="Producto")
listaStock.heading("#2", text="ID Producto")
listaStock.heading("#3", text="Modelo")
listaStock.heading("#4", text="Cantidad")
listaStock.heading("#5", text="Precio")
listaStock.column("#0", width=100)
listaStock.column("#1", width=150)
listaStock.column("#2", width=50)
listaStock.column("#3", width=300)
listaStock.column("#4", width=50)
listaStock.column("#5", width=50)

scrollbarStock = Scrollbar(ventanaTreeview, orient="vertical", command=listaStock.yview)
scrollbarStock.pack(side=LEFT)

listaStock.config(yscrollcommand= scrollbarStock.set)

for clave0Codigo, valor0Categoria in stock.items():

    for clave1Categoria, valor1Codigo in valor0Categoria.items():
        for clave2Codigo, valor2Producto in valor1Codigo.items():
            for clave3ID, valor3Detalle in valor2Producto.items():
                for clave4Detalle, valor4Tipo in valor3Detalle.items():


                    listaStock.insert("", "end", text= f"{clave1Categoria}", values=(clave3ID, clave4Detalle, valor4Tipo["Nombre"], valor4Tipo["Cantidad"], valor4Tipo["Precio"]))

modAdmin_Ventana.mainloop()