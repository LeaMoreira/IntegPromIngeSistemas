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

def fn_GuardarProveedor():
    nombreProv = nombreProveedor_Entrada.get()
    cuitProv = cuitProveedor_Entrada.get()
    direccionProv = direccionProveedor_Entrada.get()
    telefonoProv = telefonoProveedor_Entrada.get()
    productoProv = productoReferenciaProveedor_Entrada.get()

    if not cuitProv.isdigit():
        messagebox.showwarning("Advertencia", "El CUIT debe ser un número entero")
        return(cuitProveedor_Entrada)
    
    if not telefonoProv.isdigit():
        messagebox.showwarning("Advertencia", "El telefono debe ser un número entero")
        return(telefonoProveedor_Entrada)
    
    if not productoProv.isalpha():
        messagebox.showwarning("Advertencia", "La referencia debe estar escrita solo en letras")
        return(telefonoProveedor_Entrada)
    
    if nombreProv and cuitProv and direccionProv and telefonoProv and productoProv:
        if usuarios["Proveedor"]:
            usuarios["Proveedor"][nombreProv] = {
                "Direccion" : (direccionProv),
                "Numero Telefono" : int(telefonoProv),
                "Cuit" : int(cuitProv),
                "Productos" : (productoProv)
            }
        with open(rutaLogin, 'w') as archivo:
            json.dump(usuarios, archivo, indent=4)
        messagebox.showinfo("Éxito", "Producto agregado correctamente")

ventanaAltaProveedor = Tk()
ventanaAltaProveedor.title("Añadir Proveedor")

cuadroNombre = LabelFrame(ventanaAltaProveedor)
cuadroNombre.pack(fill="both", expand=True)

nombreProveedor_Texto = Label(cuadroNombre, text="Nombre")
nombreProveedor_Texto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=LEFT)

nombreProveedor_Entrada = Entry(cuadroNombre)
nombreProveedor_Entrada.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=RIGHT)

cuadroCuit = LabelFrame(ventanaAltaProveedor)
cuadroCuit.pack(fill="both", expand=True)

cuitProveedor_Texto = Label(cuadroCuit, text="CUIT")
cuitProveedor_Texto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=LEFT)

cuitProveedor_Entrada = Entry(cuadroCuit)
cuitProveedor_Entrada.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=RIGHT)

cuadroDireccion = LabelFrame(ventanaAltaProveedor)
cuadroDireccion.pack(fill="both", expand=True)

direccionProveedor_Texto = Label(cuadroDireccion, text="Direccion")
direccionProveedor_Texto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=LEFT)

direccionProveedor_Entrada = Entry(cuadroDireccion)
direccionProveedor_Entrada.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=RIGHT)

cuadroTelefono = LabelFrame(ventanaAltaProveedor)
cuadroTelefono.pack(fill="both", expand=True)

telefonoProveedor_Texto = Label(cuadroTelefono, text="Telefono")
telefonoProveedor_Texto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=LEFT)

telefonoProveedor_Entrada = Entry(cuadroTelefono)
telefonoProveedor_Entrada.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=RIGHT)

cuadroProduReferencia = LabelFrame(ventanaAltaProveedor)
cuadroProduReferencia.pack(fill="both", expand=True)

productoReferenciaProveedor_Texto = Label(cuadroProduReferencia, text="Producto Referencia")
productoReferenciaProveedor_Texto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=LEFT)

productoReferenciaProveedor_Entrada = Entry(cuadroProduReferencia)
productoReferenciaProveedor_Entrada.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=RIGHT)

cuadroBoton = LabelFrame(ventanaAltaProveedor)
cuadroBoton.pack(side= BOTTOM, fill="both", expand=True)

botonGuardar = Button(cuadroBoton, text="Guardar Proveedor", command=fn_GuardarProveedor)
botonGuardar.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=LEFT)

botonVolver = Button(cuadroBoton, text="Volver")
botonVolver.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, expand=True, side=RIGHT)


ventanaAltaProveedor.mainloop()