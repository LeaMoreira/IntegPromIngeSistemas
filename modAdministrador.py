import json
import tkinter
import modADMAgregar


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modADMAgregar import *


rutaLogin = "C:/Users/rokha/Desktop/inteProg/usuarios.json"
with open (rutaLogin, "r") as archivo:
    usuarios = json.load(archivo)

rutaStock = "C:/Users/rokha/Desktop/inteProg/productos.json"
with open (rutaStock, "r") as archivo:
    stock = json.load(archivo)

def fn_actualizarStock(listaStock):
    listaStock.delete(*listaStock.get_children())
    stock = cargarStock()

    
    for clave0, valor0 in stock.items():
        for clave1, valor1 in valor0.items():
            for clave2, valor2 in valor1.items():
                listaStock.insert("", "end", text= clave0, values=(clave1, clave2, valor2["Cantidad"], valor2["Precio"]))

def fn_modStock(ventana_Administrador, listaStock):

    def fn_CerrarVentana():
        ventana_Administrador.deiconify()
        fn_actualizarStock(listaStock)
        modAdmin_VentanaStock.destroy()    

    def fn_soloLetras(input):
        return input.isalpha()

    def fn_soloNumeros(input):
        return input.isdigit()

    modAdmin_VentanaStock = Toplevel(ventana_Administrador)
    modAdmin_VentanaStock.title("Ventana Adm STOCK")

    ventanaBotones = LabelFrame(modAdmin_VentanaStock, text="Accesibilidades: ")
    ventanaBotones.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both')

    agregar_Boton = Button(ventanaBotones, text="Agregar Producto", command= lambda: fn_modADMAgregar(modAdmin_VentanaStock, listaStock))
    agregar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand=True)

    modificar_Boton = Button(ventanaBotones, text="Modificar Producto",)
    modificar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand=True)

    eliminar_Boton = Button(ventanaBotones, text="Eliminar Producto")
    eliminar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand=True)

    modAdmin_VentanaStock.protocol("WM_DELETE_WINDOW", fn_CerrarVentana)

    
    modAdmin_VentanaStock.mainloop()