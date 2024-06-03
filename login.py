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
    
def fn_mostrarContraseña():

    if mostrarContraseña.get():
        contraseñaEntrada.config(show= "")
    else:
        contraseñaEntrada.config(show= "*")

def fn_soloLetras(input):
    return input.isalpha()

def fn_soloNumeros(input):
    return input.isdigit()

def fn_Usuario():

    usuario = usuarioEntrada.get().capitalize()
    contraseña = contraseñaEntrada.get()

    if adminSeleccion.get() == "Confirmado":

        if "Administrador" in usuarios:
            if usuario in usuarios["Administrador"] and str(usuarios["Administrador"][usuario]) == contraseña:
                messagebox.showinfo("Bienvenido", "Inicio de Sesión Exitoso")

    elif vendedorSeleccion.get() == "Confirmado":

        if "Vendedor" in usuarios:
            if usuario in usuarios["Vendedor"] and str(usuarios["Vendedor"][usuario]) == contraseña:
                messagebox.showinfo("Bienvenido", "Inicio de Sesión Exitoso")


ventanaLogin = Tk()
ventanaLogin.title("Inicio de Sesión")

validacionLetras = ventanaLogin.register(fn_soloLetras)
validacionNumero = ventanaLogin.register(fn_soloNumeros)

cuadroTexto = LabelFrame(ventanaLogin, text="Inicio De Sesión : ")
cuadroTexto.pack(padx= 5, pady= 5, ipadx= 20, ipady= 20)

usuariocuadroTexto = Label(cuadroTexto, text="Usuario:")
usuariocuadroTexto.pack(padx= 5, pady= 5)

usuarioEntrada = Entry(cuadroTexto)
usuarioEntrada.config(validate= "key", validatecommand=(validacionLetras, "%S"))
usuarioEntrada.pack(padx= 5, pady= 5)

contraseñacuadroTexto = Label(cuadroTexto, text="Contraseña:")
contraseñacuadroTexto.pack(padx= 5, pady= 5)

contraseñaEntrada = Entry(cuadroTexto, show="*")
contraseñaEntrada.config(validate= "key", validatecommand=(validacionNumero, "%S"))
contraseñaEntrada.pack(padx= 5, pady= 5)

mostrarContraseña = BooleanVar()
mostrarContraseñaCheck = Checkbutton(cuadroTexto, text="Mostrar Contraseña", variable= mostrarContraseña, command= fn_mostrarContraseña)
mostrarContraseñaCheck.pack(padx= 5, pady= 5)

cuadroTexto_CheckButton = LabelFrame(cuadroTexto)
cuadroTexto_CheckButton.pack(padx= 5, pady= 5)

adminSeleccion = StringVar()
adminSeleccionCheck = Checkbutton(cuadroTexto_CheckButton, text="Administrador", variable= adminSeleccion, onvalue="Confirmado", offvalue="No Confirmado")
adminSeleccionCheck.pack(padx= 5, pady= 5, side=LEFT)
adminSeleccionCheck.deselect()

vendedorSeleccion = StringVar()
vendedorSeleccionCheck = Checkbutton(cuadroTexto_CheckButton, text="Vendedor", variable= vendedorSeleccion, onvalue="Confirmado", offvalue="No Confirmado")
vendedorSeleccionCheck.pack(padx= 5, pady= 5, side=LEFT)
vendedorSeleccionCheck.deselect()

ingresarCuenta = Button(cuadroTexto, text="Ingresar", command= fn_Usuario)
ingresarCuenta.pack(padx= 5, pady= 5, ipadx= 45, ipady= 5)

ventanaLogin.mainloop()