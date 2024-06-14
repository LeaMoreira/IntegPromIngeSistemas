import json
import tkinter
import modAdministrador


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

rutaLogin = "C:/Users/rokha/Desktop/inteProg/usuarios.json"
with open (rutaLogin, "r") as archivo:
    usuarios = json.load(archivo)

def fn_soloNumeros(input):
    return input.isdigit()

"""
validacionNumero = ventanaLogin.register(fn_soloNumeros)
contraseñaEntrada = Entry(cuadroTexto, show="*")
contraseñaEntrada.config(validate= "key", validatecommand=(validacionNumero, "%S"))
contraseñaEntrada.pack(padx= 5, pady= 5, expand= True)
"""

ventanaProveedor = Tk()
ventanaProveedor.title("Ventana ABM de Proveedores")

listaProveedor = ttk.Treeview(ventanaProveedor, columns=("Producto","Telefono"))
listaProveedor.heading("#0", text="Proveedor")
listaProveedor.heading("#1", text="Producto")
listaProveedor.heading("#2", text="Telefono")
listaProveedor.column("#0", width=100)
listaProveedor.column("#1", width=100)
listaProveedor.column("#2", width=100)
listaProveedor.pack(ipadx= 200, ipady= 70, padx= 5, pady= 5, side= LEFT, fill='both', expand=True)

for clave0, valor0 in usuarios.items():
    if clave0 == "Proveedor":
        for clave1, valor1 in valor0.items():
            cargar = listaProveedor.insert("", "end", text=clave1, values=(valor1["Productos"],valor1["Numero Telefono"]))

cuadroBotones = LabelFrame(ventanaProveedor, text="Accesibilidades: ")
cuadroBotones.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, fill='both', expand=True)

botonAlta = Button(cuadroBotones, text="Alta Proveedor")
botonAlta.pack(ipadx= 20, ipady= 20, padx= 5, pady= 5, expand= True)

botonModificacion = Button(cuadroBotones, text="Modificar Proveedor")
botonModificacion.pack(ipadx= 5, ipady= 20, padx= 5, pady= 5, expand= True)

botonBaja = Button(cuadroBotones, text="Baja Proveedores")
botonBaja.pack(ipadx= 15, ipady= 20, padx= 5, pady= 5, expand= True)

ventanaProveedor.mainloop()