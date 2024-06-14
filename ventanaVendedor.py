import json
import tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


rutaLogin = "C:/Users/rokha/Desktop/inteProg/usuarios.json"
with open (rutaLogin, "r") as archivo:
      usuarios = json.load(archivo)

rutaStock = "C:/Users/rokha/Desktop/inteProg/productos.json"
with open (rutaStock, "r") as archivo:
      stock = json.load(archivo)

rutaVentas = ("C:/Users/rokha/Desktop/inteProg/registroVentas.json")
with open (rutaVentas, "r") as archivo:
      registroVentas = json.load(archivo)

def moduloVendedor():

    def solo_letras(input):
        return input.isalpha()

    def solo_numeros(input):
        return input.isdigit()
    

    
    
    def confirmar_compra():
        respuesta = messagebox.askquestion("Confirmar compra", "¿Estás seguro de que quieres confirmar la compra?")
        if respuesta == 'yes':
            nombre_usuario = usuarioEntrada.get().capitalize()  # Obtener el usuario ingresado
            vendedor_encontrado = None  # Inicializar vendedor_encontrado como None
            
            if "Vendedor" in usuarios:
                for vendedor_info in usuarios["Vendedor"].values():
                    if vendedor_info["Nombre"].capitalize() == nombre_usuario:
                        vendedor_encontrado = vendedor_info
                        break
            
            if vendedor_encontrado is None:
                messagebox.showerror("Error", "No se encontró el vendedor")
                return
            
            vendedor_actual = vendedor_encontrado["Nombre"]
            
            # Generar un nuevo número de compra (usando el próximo disponible)
            nuevo_numero = str(len(registroVentas["Vendedor"][vendedor_actual]["Numero"]) + 1)
            
            # Añadir los productos vendidos al registro
            for categoria, subcategorias in carro_compraDiccionario.items():
                for subcategoria, productos in subcategorias.items():
                    for producto, detalles in productos.items():
                        cantidad_vendida = detalles["Cantidad"]
                        precio_unitario = detalles["Precio"]
                        precio_total = detalles["Precio Total"]
                        
                        # Añadir la venta al registroVentas
                        registroVentas["Vendedor"][vendedor_actual]["Numero"][nuevo_numero] = {
                            producto: {
                                "Cantidad": cantidad_vendida,
                                "Precio": precio_unitario,
                                "PrecioTotal": precio_total
                            }
                        }
            
            # Guardar los cambios en el archivo JSON
            with open(rutaVentas, 'w') as archivo:
                json.dump(registroVentas, archivo, indent=4)
            
            messagebox.showinfo("Compra realizada", "La compra se realizó con éxito")
            
            # Actualizar el stock
            actualizar_stock()
            limpiar_entradas()
            return(moduloVendedor)
            
        else:
            ventana_Ventas.focus_force()

    def actualizar_stock():
        for categoria, subcategorias in carro_compraDiccionario.items():
            for subcategoria, productos in subcategorias.items():
                for producto, detalles in productos.items():
                    cantidad_vendida = detalles["Cantidad"]
                    stock[categoria][subcategoria][producto]["Cantidad"] -= cantidad_vendida

        with open(rutaStock, 'w') as archivo:
            json.dump(stock, archivo, indent= 4)

    def limpiar_entradas():
        categoria_Scroll.set('')
        producto_Scroll.set('')
        cantidad_Entrada.delete(0, 'end')
        lista_Eleccion.delete(*lista_Eleccion.get_children())
        carro_Compra.delete(*carro_Compra.get_children())
        label_total.config(text="Total: 0")

    def actualizar_subcategorias_ventas(event):
        categoria_seleccionada = categoria_Scroll.get()
        if categoria_seleccionada in stock:
            subcategorias = list(stock[categoria_seleccionada].keys())
            producto_Scroll['values'] = subcategorias
        else:
            producto_Scroll.set('')
            producto_Scroll['values'] = []

    def buscar_producto(lista_Stock):

        lista_Stock.delete(*lista_Stock.get_children())

        categoria_seleccionada = categoria_Scroll.get()

        subcategoria_seleccionada = producto_Scroll.get()

        if categoria_seleccionada and subcategoria_seleccionada:
            if categoria_seleccionada in stock and subcategoria_seleccionada in stock[categoria_seleccionada]:
                productos = stock[categoria_seleccionada][subcategoria_seleccionada]

                for nombre_producto, detalles_producto in productos.items():
                    cantidad = detalles_producto.get('Cantidad', '')
                    precio = detalles_producto.get('Precio', '')
                    lista_Stock.insert('', 'end', text=f'{categoria_seleccionada}',values=( subcategoria_seleccionada, nombre_producto, cantidad, precio))
            else:
                messagebox.showerror("Error", "La categoría o subcategoría seleccionada no es válida")
        else:
            messagebox.showerror("Error", "Por favor, seleccione una categoría y una subcategoría")

    carro_compraDiccionario = {} 

    def calcular_total():
        total = sum(float(carro_Compra.item(item, "values")[2]) for item in carro_Compra.get_children())
        label_total.config(text=f"Total: {total}")

    def agregar_al_carro():

        item_seleccionado = lista_Eleccion.focus()
        if not item_seleccionado:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto para agregarlo al carrito")
            return

        cantidad_seleccionada = cantidad_Entrada.get()
        if not cantidad_seleccionada.isdigit():
            messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero")
            return

        cantidad_seleccionada = int(cantidad_seleccionada)
        if cantidad_seleccionada <= 0:
            messagebox.showwarning("Advertencia", "La cantidad debe ser mayor que cero")
            return
        
        cantidad_Disponible = int(lista_Eleccion.item(item_seleccionado, "values")[2])

        if cantidad_seleccionada > cantidad_Disponible:
            messagebox.showwarning("Advertencia", "La cantidad ingresada es mayor que la cantidad disponible en stock")
            return

        
        nombre_producto_seleccionado = lista_Eleccion.item(item_seleccionado, "values")[1] # SACAMOS EL NOMBRE DEL PRODUCTO CON valor[1]
        categoria_seleccionada = lista_Eleccion.item(item_seleccionado, "text") # DE QUE CATEGORIA SE ELIGIO EL PRODUCTO
        subcategoria_seleccionada = lista_Eleccion.item(item_seleccionado, "values")[0] # SACAMOS DE QUE CATEGORIA CON valor [0]
        precio_unitario = float(lista_Eleccion.item(item_seleccionado, "values")[3]) # PRECIO
        precio_Total = precio_unitario * cantidad_seleccionada

        producto_agregado = {
            "Cantidad": cantidad_seleccionada,
            "Precio": precio_unitario,
            "Precio Total": precio_Total
        }

        if categoria_seleccionada not in carro_compraDiccionario:
            carro_compraDiccionario[categoria_seleccionada] = {}

        if subcategoria_seleccionada not in carro_compraDiccionario[categoria_seleccionada]:
            carro_compraDiccionario[categoria_seleccionada][subcategoria_seleccionada] = {}

        carro_compraDiccionario[categoria_seleccionada][subcategoria_seleccionada][nombre_producto_seleccionado] = producto_agregado

        actualizar_carro_de_compras()
        calcular_total()

    def actualizar_carro_de_compras():

        for item in carro_Compra.get_children():
            carro_Compra.delete(item)

        if not carro_compraDiccionario:
            return

        for categoria, subcategorias in carro_compraDiccionario.items():
            for subcategoria, productos in subcategorias.items():
                for producto, detalles in productos.items():
                    cantidad = detalles["Cantidad"]
                    precio = detalles["Precio"]
                    precio_Total = detalles["Precio Total"]
                    carro_Compra.insert("", "end", text=producto, values=(cantidad, precio, precio_Total))

    def quitar_del_carro():

        item_seleccionado = carro_Compra.focus()

        if not item_seleccionado:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto para quitarlo del carrito")
            return

        nombre_producto_seleccionado = carro_Compra.item(item_seleccionado, "text")
        
        for categoria, subcategorias in carro_compraDiccionario.items():
            for subcategoria, productos in subcategorias.items():
                if nombre_producto_seleccionado in productos:
                    del carro_compraDiccionario[categoria][subcategoria][nombre_producto_seleccionado]
                    break

        actualizar_carro_de_compras()  
        calcular_total()

    def volver_Adm():
        ventana_Ventas.withdraw()

        
    ventana_Ventas = Tk()
    ventana_Ventas.title('Ventana de Vendedor')
    ventana_Ventas.geometry('900x650')

    usuarioEntrada = Entry(ventana_Ventas)
    usuarioEntrada.place(x=350, y=50, width=150, height=30)

    categoria_texto = Label(ventana_Ventas, text='Categoria')
    categoria_texto.place(x=20, y=20, width=150, height=30)

    producto_texto = Label(ventana_Ventas, text='Producto')
    producto_texto.place(x=180, y=20, width=150, height=30)

    categoria_Scroll = ttk.Combobox(ventana_Ventas)
    categoria_Scroll.place(x=20, y=50, width=150, height=30)
    categoria_Scroll['values'] = list(stock.keys())
    categoria_Scroll.bind("<<ComboboxSelected>>", actualizar_subcategorias_ventas)

    producto_Scroll = ttk.Combobox(ventana_Ventas)
    producto_Scroll.place(x=180, y=50, width=150, height=30)

    busqueda = Button(ventana_Ventas, text='Buscar', command=lambda: buscar_producto(lista_Eleccion))
    busqueda.place(x=770, y=40, width=100, height=50)


    lista_Eleccion = ttk.Treeview(ventana_Ventas, columns=('Categoria','Producto','Cantidad','Precio'))
    lista_Eleccion.place(x=20, y=110, width='850', height='200')
    lista_Eleccion.heading('#0',text='Categoria')
    lista_Eleccion.heading('#1',text='Producto')
    lista_Eleccion.heading('#2',text='Modelo')
    lista_Eleccion.heading('#3',text='Cantidad')
    lista_Eleccion.heading('#4',text='Precio')
    lista_Eleccion.column('#0', width=100)
    lista_Eleccion.column('#1', width=150)
    lista_Eleccion.column('#2', width=300)                
    lista_Eleccion.column('#3', width=50)
    lista_Eleccion.column('#4', width=50)

    validacion_numeros = ventana_Ventas.register(solo_numeros)

    añadir_Carro = Button(ventana_Ventas, text='Añadir', command=agregar_al_carro)
    añadir_Carro.place(x=770, y=320, width=100, height=50)

    cantidad_Texto = Label(ventana_Ventas, text='Unidades')
    cantidad_Texto.place(x=710, y=325, width=50, height=20)

    cantidad_Entrada = Entry(ventana_Ventas)
    cantidad_Entrada.config(validate="key", validatecommand=(validacion_numeros, '%S'))
    cantidad_Entrada.place(x=710, y=350, width=50, height=20)

    carro_CompraTexto = Label(ventana_Ventas, text='Carro de Compras Cliente')
    carro_CompraTexto.place(x=70, y=320, width=200, height=30)

    carro_Compra = ttk.Treeview( ventana_Ventas, columns=('Cantidad', 'PxUnidad', 'Precio Total'))
    carro_Compra.place(x=20, y=360, width='550', height='200')
    carro_Compra.heading('#0', text='Producto')
    carro_Compra.heading('#1', text='Cantidad')
    carro_Compra.heading('#2', text='PxUnidad')
    carro_Compra.heading('#3', text='Precio Total')
    carro_Compra.column('#0', width=300)
    carro_Compra.column('#1', width=50)
    carro_Compra.column('#2', width=100)
    carro_Compra.column('#3', width=100)

    label_total = Label(ventana_Ventas, text="Total: 0")
    label_total.place(x=20, y=570, width=100, height=30)

    scrollbar_carro = Scrollbar(ventana_Ventas, orient="vertical", command=carro_Compra.yview)
    scrollbar_carro.place(x=570, y=360, height=200)

    carro_Compra.config(yscrollcommand=scrollbar_carro.set)

    borrar_Carro = Button(ventana_Ventas, text='Quitar', command=quitar_del_carro)
    borrar_Carro.place(x=360, y=570, width=100, height=30)

    compra_Boton = Button(ventana_Ventas, text='Confirmar', command= confirmar_compra)
    compra_Boton.place(x=470, y=570, width=100, height=30)

    volver_Boton = Button(ventana_Ventas, text="Volver", command= volver_Adm)
    volver_Boton.place(x=470, y=610, width=100, height=30)


    ventana_Ventas.mainloop()
