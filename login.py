import json
import tkinter
import ventanaAdministrador
import ventanaVendedor
import modAdministrador
import configuracion

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ventanaAdministrador import moduloAdministrador
from ventanaAdministrador import *
from ventanaVendedor import moduloVendedor
from configuracion import *

rutaLogin = "C:/Users/rokha/Desktop/inteProg/usuarios.json"
with open (rutaLogin, "r") as archivo:
    usuarios = json.load(archivo)

rutaStock = "C:/Users/rokha/Desktop/inteProg/productos.json"
with open (rutaStock, "r") as archivo:
    stock = json.load(archivo)

rutaVentas = ("C:/Users/rokha/Desktop/inteProg/registroVentas.json")
with open (rutaVentas, "r") as archivo:
      registroVentas = json.load(archivo)
    
def fn_mostrarContraseña():

    if mostrarContraseña.get():
        contraseñaEntrada.config(show= "")
    else:
        contraseñaEntrada.config(show= "*")

def fn_soloLetras(input):
    return input.isalpha()

def solo_numeros(input):
    return input.isdigit()

def fn_Usuario():

    usuario = usuarioEntrada.get().capitalize()
    contraseña = contraseñaEntrada.get()

    if adminSeleccion.get() == "Confirmado" and vendedorSeleccion.get() == "No Confirmado":

        if "Administrador" in usuarios:
            if usuario in usuarios["Administrador"] and str(usuarios["Administrador"][usuario]) == contraseña:
                messagebox.showinfo("Bienvenido", "Inicio de Sesión Exitoso")
                moduloAdministrador()
                ventanaLogin.withdraw()
            
            else:
                messagebox.showerror('Error', 'Credenciales incorrectas o usuario no registrado')
        else:
            messagebox.showerror('Error', 'No hay usuarios administradores registrados')

    elif vendedorSeleccion.get() == "Confirmado" and adminSeleccion.get() == "No Confirmado":

        if "Vendedor" in usuarios:
            for vendedor_info in usuarios["Vendedor"].values():
                if vendedor_info["Nombre"].capitalize() == usuario.capitalize() and str(vendedor_info["Contrasena"]) == contraseña:
                    vendedor_encontrado = vendedor_info
                    break

            if vendedor_encontrado:
                messagebox.showinfo("Bienvenido", "Inicio de Sesión Exitoso")
                moduloVendedor()
                ventanaLogin.withdraw()

            else:
                messagebox.showerror('Error', 'Credenciales incorrectas')
        else:
                messagebox.showerror('Error', 'Usuario no registrado como vendedor')    
    else:
            messagebox.showerror("Error", "Debe seleccionar solo una forma de logeo, Administrador o Vendedor")


ventanaLogin = Tk()
ventanaLogin.title("Inicio de Sesión")

validacionLetras = ventanaLogin.register(fn_soloLetras)
validacionNumero = ventanaLogin.register(solo_numeros)

cuadroTexto = LabelFrame(ventanaLogin, text="Inicio De Sesión : ")
cuadroTexto.pack(padx= 5, pady= 5, ipadx= 20, ipady= 20, fill="both")

usuariocuadroTexto = Label(cuadroTexto, text="Usuario:")
usuariocuadroTexto.pack(padx= 5, pady= 5, expand= True)

usuarioEntrada = Entry(cuadroTexto)
usuarioEntrada.config(validate= "key", validatecommand=(validacionLetras, "%S"))
usuarioEntrada.pack(padx= 5, pady= 5, expand= True)

contraseñacuadroTexto = Label(cuadroTexto, text="Contraseña:")
contraseñacuadroTexto.pack(padx= 5, pady= 5, expand= True)

contraseñaEntrada = Entry(cuadroTexto, show="*")
contraseñaEntrada.config(validate= "key", validatecommand=(validacionNumero, "%S"))
contraseñaEntrada.pack(padx= 5, pady= 5, expand= True)

mostrarContraseña = BooleanVar()
mostrarContraseñaCheck = Checkbutton(cuadroTexto, text="Mostrar Contraseña", variable= mostrarContraseña, command= fn_mostrarContraseña)
mostrarContraseñaCheck.pack(padx= 5, pady= 5, expand= True)

cuadroTexto_CheckButton = LabelFrame(cuadroTexto)
cuadroTexto_CheckButton.pack(padx= 5, pady= 5, fill="both")

adminSeleccion = StringVar()
adminSeleccionCheck = Checkbutton(cuadroTexto_CheckButton, text="Administrador", variable= adminSeleccion, onvalue="Confirmado", offvalue="No Confirmado")
adminSeleccionCheck.pack(padx= 5, pady= 5, side=LEFT)
adminSeleccionCheck.deselect()

vendedorSeleccion = StringVar()
vendedorSeleccionCheck = Checkbutton(cuadroTexto_CheckButton, text="Vendedor", variable= vendedorSeleccion, onvalue="Confirmado", offvalue="No Confirmado")
vendedorSeleccionCheck.pack(padx= 5, pady= 5, side=LEFT)
vendedorSeleccionCheck.deselect()

ingresarCuenta = Button(cuadroTexto, text="Ingresar", command= fn_Usuario)
ingresarCuenta.pack(padx= 5, pady= 5, ipadx= 45, ipady= 5, expand= True)

ventanaLogin.mainloop()