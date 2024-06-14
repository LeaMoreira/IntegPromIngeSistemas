import json
import tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from configuracion import rutaStock, cargarStock, guardarStock

rutaLogin = "C:/Users/rokha/Desktop/inteProg/usuarios.json"
with open (rutaLogin, "r") as archivo:
    usuarios = json.load(archivo)

rutaStock = "C:/Users/rokha/Desktop/inteProg/productos.json"
with open (rutaStock, "r") as archivo:
    stock = json.load(archivo)

def fn_modADMAgregar(parent, listaStock):

    def fn_soloNumeros(input):
        return input.isdigit()
    
    def fn_actualizarStock(listaStock):
        listaStock.delete(*listaStock.get_children())
        stock = cargarStock()

        
        for clave0, valor0 in stock.items():
            for clave1, valor1 in valor0.items():
                for clave2, valor2 in valor1.items():
                    listaStock.insert("", "end", text= clave0, values=(clave1, clave2, valor2["Cantidad"], valor2["Precio"]))

    def fn_guardarProducto():
        categoriaSeleccionada = categoriaCombobox.get()
        seccionSeleccionada = seccionCombobox.get()
        nombreProducto = nombre_entry.get()
        cantidadProducto = cantidad_entry.get()
        precioProducto = precio_entry.get()

        if not cantidadProducto.isdigit():
            messagebox.showwarning("Advertencia", "La cantidad seleccionada debe ser un número entero")
            return(cantidad_entry)
        cantidadProducto = int(cantidadProducto)
        if cantidadProducto <= 0:
            messagebox.showwarning("Advertencia", "La cantidad debe ser mayor que cero")
            return(cantidad_entry)
        
        precioProducto = float(precioProducto)
        if precioProducto <= 0:
            messagebox.showwarning("Advertencia", "El precio debe ser mayor que cero")
            return
        
        if nombreProducto and cantidadProducto and precioProducto:
            stock = cargarStock()
            if categoriaSeleccionada in stock and seccionSeleccionada in stock[categoriaSeleccionada]:
                stock[categoriaSeleccionada][seccionSeleccionada][nombreProducto] = {
                    "Cantidad" : int(cantidadProducto),
                    "Precio" : float(precioProducto)
                }

                guardarStock(archivo)
                messagebox.showwarning("Éxtio", "Producto agregado correctamete")

                ventanaAñadirProducto.destroy()
                fn_actualizarStock(listaStock)
                
        


    ventanaAñadirProducto = Tk()
    ventanaAñadirProducto.title("Añadir Producto")

    validacionNumero = ventanaAñadirProducto.register(fn_soloNumeros)

    cuadroCombobox = LabelFrame(ventanaAñadirProducto, text="Elección de Secciones: ")
    cuadroCombobox.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill= "both")

    categoriaTexto = Label(cuadroCombobox, text="Categoría")
    categoriaTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand= True)
    categoriaCombobox = ttk.Combobox(cuadroCombobox, values= list(stock.keys()))
    categoriaCombobox.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand= True)

    seccionTexto = Label(cuadroCombobox, text="Seccion")
    seccionTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand= True)
    seccionCombobox = ttk.Combobox(cuadroCombobox)
    seccionCombobox.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand= True)

    cuadroEntradas = LabelFrame(ventanaAñadirProducto, text="Producto Nuevo: ")
    cuadroEntradas.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill= "both")

    nombre_label = Label(cuadroEntradas, text="Nombre del producto:")
    nombre_label.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)
    nombre_entry = Entry(cuadroEntradas)
    nombre_entry.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

    cantidad_label = Label(cuadroEntradas, text="Cantidad en stock:")
    cantidad_label.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)
    cantidad_entry = Entry(cuadroEntradas, validate="key", validatecommand=(validacionNumero, '%S'))
    cantidad_entry.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

    precio_label = Label(cuadroEntradas, text="Precio del producto:")
    precio_label.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)
    precio_entry = Entry(cuadroEntradas, validate="key", validatecommand=(validacionNumero, '%S'))
    precio_entry.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

    cuadroBotones = LabelFrame(ventanaAñadirProducto)
    cuadroBotones.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill= "both")

    botonGuardar = Button(cuadroBotones, text="Guardar", command= fn_guardarProducto)
    botonGuardar.pack(ipadx= 40, ipady= 5, padx= 5, pady= 5, fill= "y")

    botonVolver = Button(cuadroBotones, text="Volver")
    botonVolver.pack(ipadx= 45, ipady= 5, padx= 5, pady= 5, fill= "y")

    def fn_ActualizarSubcategorias(event):

        categoriaSeleccionada = categoriaCombobox.get()
        if categoriaSeleccionada in stock:
            seccion = list(stock[categoriaSeleccionada].keys())
            seccionCombobox["values"] = seccion
        else:
            seccionCombobox.set("")
            seccionCombobox["values"] = []

    categoriaCombobox.bind("<<ComboboxSelected>>", fn_ActualizarSubcategorias)
            

    ventanaAñadirProducto.mainloop()