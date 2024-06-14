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

def moduloAdministrador():

      def fn_soloLetras(input):
            return input.isalpha()

      def fn_soloNumeros(input):
            return input.isdigit()

      def actualizarStock():
            
            listaStock.delete(*listaStock.get_children())

            with open (rutaStock, "r") as archivo:
                  stockActualizado = json.load(archivo)

            for clave0, valor0 in stockActualizado.items():
                  for clave1, valor1 in valor0.items():
                        for clave2, valor2 in valor1.items():
                              stockActualizado = listaStock.insert("", "end", text= clave0, values=(clave1, clave2, valor2["Cantidad"], valor2["Precio"]))

      def actualizarVendedor():
            
            listaVendedor.delete(*listaVendedor.get_children())

            with open(rutaLogin, "r") as archivo:
                  loginActualizado = json.load(archivo)

            if "Vendedor" in loginActualizado:
                  for vendedorClave0, vendedorValor0 in loginActualizado["Vendedor"].items():
                        listaVendedor.insert("", "end", text=vendedorClave0, values=(vendedorValor0["Nombre"]))

      def salir():
            ventana_Administrador.withdraw()

      def agregar_producto():

            def guardar_producto():

                  categoriaSeleccionada = categoria_combobox.get()
                  subcategoriaSeleccionada = subcategoria_combobox.get()
                  nombreProducto = nombre_entry.get()
                  cantidadProducto = cantidad_entry.get()
                  precioProducto = precio_entry.get()

                  if nombreProducto and cantidadProducto and precioProducto:
                        if categoriaSeleccionada in stock and subcategoriaSeleccionada in stock[categoriaSeleccionada]:
                              stock[categoriaSeleccionada][subcategoriaSeleccionada][nombreProducto] = {
                              "Cantidad": int(cantidadProducto),
                              "Precio": int(precioProducto)
                              }
                              with open(rutaStock, 'w') as archivo:
                                    json.dump(stock, archivo, indent=4)
                              messagebox.showinfo("Éxito", "Producto agregado correctamente")

                              ventana_NuevoProducto.destroy()
                              
                              actualizarStock()
                        else:
                              messagebox.showerror("Error", "La categoría o subcategoría seleccionada no es válida")
                  else:
                        messagebox.showerror("Error", "Por favor, complete todos los campos")

            ventana_NuevoProducto = Tk()
            ventana_NuevoProducto.title("Añadir Producto")
            ventana_NuevoProducto.geometry("320x400")
            
            categoria_label = Label(ventana_NuevoProducto, text="Categoría:")
            categoria_label.place(x=80, y=40, width=150, height=20)
            categoria_combobox = ttk.Combobox(ventana_NuevoProducto, values=list(stock.keys()))
            categoria_combobox.place(x=105, y=70, width=100, height=20)

            subcategoria_label = Label(ventana_NuevoProducto, text="Subcategoría:")
            subcategoria_label.place(x=80, y=100, width=150, height=20)
            subcategoria_combobox = ttk.Combobox(ventana_NuevoProducto)
            subcategoria_combobox.place(x=105, y=130, width=100, height=20)

            nombre_label = Label(ventana_NuevoProducto, text="Nombre del producto:")
            nombre_label.place(x=80, y=160, width=150, height=20)
            nombre_entry = Entry(ventana_NuevoProducto)
            nombre_entry.place(x=5, y=190, width=300, height=20)

            cantidad_label = Label(ventana_NuevoProducto, text="Cantidad en stock:")
            cantidad_label.place(x=5, y=220, width=150, height=20)
            cantidad_entry = Entry(ventana_NuevoProducto)
            cantidad_entry.place(x=30, y=250, width=100, height=20)

            precio_label = Label(ventana_NuevoProducto, text="Precio del producto:")
            precio_label.place(x=165, y=220, width=150, height=20)
            precio_entry = Entry(ventana_NuevoProducto)
            precio_entry.place(x=190, y=250, width=100, height=20)

            def actualizar_subcategorias(event):

                  categoriaSeleccionada = categoria_combobox.get()
                  if categoriaSeleccionada in stock:
                        subcategorias = list(stock[categoriaSeleccionada].keys())
                        subcategoria_combobox['values'] = subcategorias
                  else:
                        subcategoria_combobox.set('')
                        subcategoria_combobox['values'] = []

            categoria_combobox.bind("<<ComboboxSelected>>", actualizar_subcategorias)

            guardar_button = Button(ventana_NuevoProducto, text="Guardar", command=guardar_producto)
            guardar_button.place(x=110, y=290, width=100, height=40)

            ventana_NuevoProducto.mainloop()

      def modificar_producto():

            seleccion = listaStock.selection()
            if not seleccion:
                  messagebox.showwarning("Advertencia", "Debe seleccionar un producto para modificarlo")
                  return
            
            with open(rutaStock, "r") as archivo:
                  stockActual = json.load(archivo)

                  item_seleccionado = listaStock.focus()
                  categoriaSeleccionada = listaStock.item(item_seleccionado, "text")
                  subcategoriaSeleccionada = listaStock.item(item_seleccionado, "values")[0]
                  nombreProducto_seleccionado = listaStock.item(item_seleccionado, "values")[1]

                  producto = stockActual[categoriaSeleccionada][subcategoriaSeleccionada][nombreProducto_seleccionado]
                  cantidadActual = producto["Cantidad"]
                  precioActual = producto["Precio"]

            def guardar_cambios():
            
                  cantidad_nueva = cantidad_ProduModificar.get()
                  precio_nuevo = precio_ProduModificar.get()

                  if cantidad_nueva and precio_nuevo:

                        seleccion = listaStock.selection()
                        if not seleccion:
                              messagebox.showwarning("Advertencia", "Debe seleccionar un producto para modificarlo")
                              return
                        
                        stock[categoriaSeleccionada][subcategoriaSeleccionada][nombreProducto_seleccionado]["Cantidad"] = int(cantidad_nueva)
                        stock[categoriaSeleccionada][subcategoriaSeleccionada][nombreProducto_seleccionado]["Precio"] = int(precio_nuevo)

                        with open(rutaStock, 'w') as archivo:
                              json.dump(stock, archivo, indent=4)

                        actualizarStock()
                        
                        messagebox.showinfo("Éxito", "Los cambios han sido guardados exitosamente")
                        window_ModificarProducto.destroy()
                  else:
                        messagebox.showerror("Error", "Por favor, complete todos los campos")

            window_ModificarProducto = Tk()
            window_ModificarProducto.title("Modificar Producto")
            window_ModificarProducto.geometry("300x300")

            item_seleccionado = listaStock.focus()
            nombreProducto_seleccionado = listaStock.item(item_seleccionado, "values")[1]
            etiqueta_Producto = Label(window_ModificarProducto, text=f"{nombreProducto_seleccionado}")
            etiqueta_Producto.place(x=5, y=20, width=300, height=20)

            cantidad_Label = Label(window_ModificarProducto, text="Nueva Cantidad:")
            cantidad_Label.place(x=100, y=50, width=100, height=20)
            cantidad_ProduModificar = Entry(window_ModificarProducto)
            cantidad_ProduModificar.place(x=100, y=80, width=100, height=20)
            cantidad_ProduModificar.insert(0, cantidadActual)

            precio_Label = Label(window_ModificarProducto, text="Nuevo Precio:")
            precio_Label.place(x=100, y=110, width=100, height=20)
            precio_ProduModificar = Entry(window_ModificarProducto)
            precio_ProduModificar.place(x=100, y=140, width=100, height=20)
            precio_ProduModificar.insert(0, precioActual)

            guardar_button = Button(window_ModificarProducto, text="Guardar Cambios", command=guardar_cambios)
            guardar_button.place(x=100, y=180, width=100, height=40)

            window_ModificarProducto.mainloop()

      def eliminar_producto():

            seleccion_producto = listaStock.selection()
            if not seleccion_producto:
                  messagebox.showwarning("Advertencia", "Debe seleccionar un producto para poder eliminarlo")
                  return
            
            respuesta = messagebox.askquestion("Confirmar", "¿Desea eliminar este producto?")
            if respuesta == "yes":  
                  item_seleccionado = listaStock.focus()
                  nombreProducto_seleccionado = listaStock.item(item_seleccionado, "values")[1]
                  categoria_producto_seleccionado = listaStock.item(item_seleccionado, "text")
                  encontrado = False
                  for categoria, productos in stock.items():
                        for subcategoria, subproductos in productos.items():
                              for nombre, detalles in subproductos.items():
                                    if nombre == nombreProducto_seleccionado:
                                          del stock[categoria][subcategoria][nombre]
                                          encontrado = True
                                          break
                              if encontrado:
                                    break
                        if encontrado:
                              break
                  
                  if encontrado:
                        messagebox.showinfo("Éxito", f"El producto '{nombreProducto_seleccionado}' ha sido eliminado")
                  
                        with open(rutaStock, 'w') as archivo:
                              json.dump(stock, archivo, indent=4)
                        
                        actualizarStock()
                  else:
                        messagebox.showerror("Error", "El producto seleccionado no existe en la categoría")
            else:
                  ventana_Administrador.focus_force()

      def modificarVendedor():
      
            def actualizarListaVendedor():
                  listaVendedor_Modificar.delete(*listaVendedor_Modificar.get_children())

                  with open(rutaLogin, "r") as archivo:
                        usuarioActualizado = json.load(archivo)

                  if "Vendedor" in usuarioActualizado:
                        for vendedor, codigo in usuarioActualizado["Vendedor"].items():
                              listaVendedor_Modificar.insert("", "end", text= f"{vendedor}", values=(codigo["Nombre"], codigo["Apellido"], codigo["Contrasena"], codigo["DNI"], codigo["Direccion"], codigo["Telefono"]))

            def botonAñadirVendedor():

                  def volver():
                        ventana_NuevoVendedor.withdraw()
                        ventanaListaVendedor.deiconify()

                  def guardar_NuevoVendedor():

                        nuevoNombre = nombreRegistro.get()
                        nuevoApellido = apellidoRegistro.get()
                        nuevaContraseña = contraseñaRegistro.get()
                        nuevoDni = dniRegistro.get()
                        nuevaDireccion = direccionRegistro.get()
                        nuevoTelefono = telefonoRegistro.get()

                        if nuevoNombre and nuevoApellido and nuevaContraseña and nuevoDni and nuevaDireccion and nuevoTelefono:
                              with open(rutaLogin, "r") as archivo:
                                    usuarios = json.load(archivo)

                              nuevoID = max([int(i) for i in usuarios["Vendedor"].keys()]) + 1

                              usuarios["Vendedor"][str(nuevoID)] = {
                                    "Nombre": nuevoNombre,
                                    "Apellido": nuevoApellido,
                                    "Contrasena": nuevaContraseña,
                                    "DNI": nuevoDni,
                                    "Direccion": nuevaDireccion,
                                    "Telefono": nuevoTelefono
                              }
                              with open(rutaLogin, "w") as archivo:
                                    json.dump(usuarios, archivo, indent= 4)
                              
                              actualizarListaVendedor()

                              messagebox.showinfo("Exito", "Vendedor Agregado")
                              ventana_NuevoVendedor.withdraw()
                              ventanaListaVendedor.deiconify()     
                        else:
                              messagebox.showerror("Error", "Por favor, Complete todos los campos")


                  ventana_NuevoVendedor = Tk()
                  ventana_NuevoVendedor.title("Nuevo Vendedor")

                  validacionLetras = ventana_NuevoVendedor.register(fn_soloLetras)
                  validacionNumero = ventana_NuevoVendedor.register(fn_soloNumeros)

                  nombreTexto = Label(ventana_NuevoVendedor, text="Nombre")
                  nombreTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  nombreRegistro = Entry(ventana_NuevoVendedor)
                  nombreRegistro.config(validate= "key", validatecommand=(validacionLetras, "%S"))
                  nombreRegistro.pack(ipadx= 5, padx= 5)

                  apellidoTexto = Label(ventana_NuevoVendedor, text="Apellido")
                  apellidoTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  apellidoRegistro = Entry(ventana_NuevoVendedor)
                  apellidoRegistro.config(validate= "key", validatecommand=(validacionLetras, "%S"))
                  apellidoRegistro.pack(ipadx= 5, padx= 5)

                  contraseñaTexto = Label(ventana_NuevoVendedor, text="Contraseña")
                  contraseñaTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  contraseñaRegistro = Entry(ventana_NuevoVendedor)
                  contraseñaRegistro.config(validate= "key", validatecommand=(validacionNumero, "%S"))
                  contraseñaRegistro.pack(ipadx= 5, padx= 5)

                  dniTexto = Label(ventana_NuevoVendedor, text="DNI")
                  dniTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  dniRegistro = Entry(ventana_NuevoVendedor)
                  dniRegistro.config(validate= "key", validatecommand=(validacionNumero, "%S"))
                  dniRegistro.pack(ipadx= 5, padx= 5)

                  direccionTexto = Label(ventana_NuevoVendedor, text="Direccion")
                  direccionTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  direccionRegistro = Entry(ventana_NuevoVendedor)
                  direccionRegistro.pack(ipadx= 5, padx= 5)

                  telefonoTexto = Label(ventana_NuevoVendedor, text="Telefono")
                  telefonoTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  telefonoRegistro = Entry(ventana_NuevoVendedor)
                  telefonoRegistro.config(validate= "key", validatecommand=(validacionNumero, "%S"))
                  telefonoRegistro.pack(ipadx= 5, padx= 5)

                  cuadroGuardarSalir = LabelFrame(ventana_NuevoVendedor)
                  cuadroGuardarSalir.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  botonGuardar = Button(cuadroGuardarSalir, text="Guardar", command= guardar_NuevoVendedor)
                  botonGuardar.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT)

                  botonSalir = Button(cuadroGuardarSalir, text="Salir", command=volver)
                  botonSalir.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT)

                  ventana_NuevoVendedor.mainloop()
            
            def modificar_NuevoVendedor():
                  seleccion = listaVendedor_Modificar.selection()
                  if not seleccion:
                        messagebox.showwarning("Advertencia", "Debe seleccionar un Vendedor de la lista")
                        return

                  def volver():
                        actualizarVendedor()
                        ventana_ModificarVendedor.withdraw()
                        ventanaListaVendedor.deiconify()

                  def guardar_Vendedor():
                        nombreMod = nombreEntrada.get()
                        apellidoMod = apellidoEntrada.get()
                        contraseñaMod = contraseñaEntrada.get()
                        DniMod = dniEntrada.get()
                        direccionMod = direccionEntrada.get()
                        telefonoMod = telefonoEntrada.get()

                        if nombreMod and apellidoMod and contraseñaMod and DniMod and direccionMod and telefonoMod:
                              seleccion = listaVendedor_Modificar.focus()
                              idSeleccionado = listaVendedor_Modificar.item(seleccion, "values")[0]
                              vendedorSeleccionado = listaVendedor_Modificar.item(seleccion, "values")[1]
                              print(seleccion, idSeleccionado, vendedorSeleccionado)


                              vendedor_id = None

                              # Buscar el vendedor en el JSON basado en el nombre
                              for id in usuarios["Vendedor"].items():
                                    for vendedor in id.items():
                                          if vendedor["Nombre"] == vendedorSeleccionado:
                                                vendedor_id = id
                                                break

                              if vendedor_id:
                                    usuarios["Vendedor"][vendedor_id]["Nombre"] = nombreMod
                                    usuarios["Vendedor"][vendedor_id]["Apellido"] = apellidoMod
                                    usuarios["Vendedor"][vendedor_id]["Contrasena"] = int(contraseñaMod)
                                    usuarios["Vendedor"][vendedor_id]["DNI"] = int(DniMod)
                                    usuarios["Vendedor"][vendedor_id]["Direccion"] = direccionMod
                                    usuarios["Vendedor"][vendedor_id]["Telefono"] = int(telefonoMod)

                                    with open(rutaLogin, "w") as archivo:
                                          json.dump(usuarios, archivo, indent=4)

                                    actualizarListaVendedor()

                                    messagebox.showinfo("Éxito", "Vendedor modificado correctamente")
                                    ventana_ModificarVendedor.withdraw()
                                    ventanaListaVendedor.deiconify()
                              else:
                                    messagebox.showerror("Error", f"El vendedor con ID {vendedorSeleccionado} no existe.")
                        else:
                              messagebox.showerror("Error", "Por favor, complete todos los campos.")           

                  ventana_ModificarVendedor = Tk()
                  ventana_ModificarVendedor.title("Modificar Datos Vendedor")
                  
                  validacionLetras = ventana_ModificarVendedor.register(fn_soloLetras)
                  validacionNumero = ventana_ModificarVendedor.register(fn_soloNumeros)

                  nombreTexto = Label(ventana_ModificarVendedor, text="Nombre")
                  nombreTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  nombreEntrada = Entry(ventana_ModificarVendedor)
                  nombreEntrada.config(validate= "key", validatecommand=(validacionLetras, "%S"))
                  nombreEntrada.pack(ipadx= 5, padx= 5)

                  apellidoTexto = Label(ventana_ModificarVendedor, text="Apellido")
                  apellidoTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  apellidoEntrada = Entry(ventana_ModificarVendedor)
                  apellidoEntrada.config(validate= "key", validatecommand=(validacionLetras, "%S"))
                  apellidoEntrada.pack(ipadx= 5, padx= 5)

                  contraseñaTexto = Label(ventana_ModificarVendedor, text="Contraseña")
                  contraseñaTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  contraseñaEntrada = Entry(ventana_ModificarVendedor)
                  contraseñaEntrada.config(validate= "key", validatecommand=(validacionNumero, "%S"))
                  contraseñaEntrada.pack(ipadx= 5, padx= 5)

                  dniTexto = Label(ventana_ModificarVendedor, text="DNI")
                  dniTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  dniEntrada = Entry(ventana_ModificarVendedor)
                  dniEntrada.config(validate= "key", validatecommand=(validacionNumero, "%S"))
                  dniEntrada.pack(ipadx= 5, padx= 5)

                  direccionTexto = Label(ventana_ModificarVendedor, text="Direccion")
                  direccionTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  direccionEntrada = Entry(ventana_ModificarVendedor)
                  direccionEntrada.pack(ipadx= 5, padx= 5)

                  telefonoTexto = Label(ventana_ModificarVendedor, text="Telefono")
                  telefonoTexto.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  telefonoEntrada = Entry(ventana_ModificarVendedor)
                  telefonoEntrada.config(validate= "key", validatecommand=(validacionNumero, "%S"))
                  telefonoEntrada.pack(ipadx= 5, padx= 5)

                  cuadroGuardarSalir = LabelFrame(ventana_ModificarVendedor)
                  cuadroGuardarSalir.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5)

                  botonGuardar = Button(cuadroGuardarSalir, text="Guardar", command= guardar_Vendedor)
                  botonGuardar.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT)

                  botonSalir = Button(cuadroGuardarSalir, text="Salir", command=volver)
                  botonSalir.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT)

                  itemSeleccionado = listaVendedor_Modificar.focus()
                  vendedorSeleccionado = listaVendedor_Modificar.item(itemSeleccionado, "values")[0]  # Obtener el nombre seleccionado

                  vendedor_id = None
                  vendedor_datos = None

                  # Buscar el vendedor en el JSON basado en el nombre
                  for id, vendedor in usuarios["Vendedor"].items():
                        if vendedor["Nombre"] == vendedorSeleccionado:
                              vendedor_id = id
                              vendedor_datos = vendedor
                              break

                  if vendedor_datos:
                        nombreEntrada.insert(0, vendedor_datos.get("Nombre", ""))
                        apellidoEntrada.insert(0, vendedor_datos.get("Apellido", ""))
                        contraseñaEntrada.insert(0, vendedor_datos.get("Contrasena", ""))
                        dniEntrada.insert(0, vendedor_datos.get("DNI", ""))
                        direccionEntrada.insert(0, vendedor_datos.get("Direccion", ""))
                        telefonoEntrada.insert(0, vendedor_datos.get("Telefono", ""))
                  else:
                        messagebox.showerror("Error", f"El vendedor con nombre {vendedorSeleccionado} no existe.")

                  ventana_ModificarVendedor.mainloop()

            
            def eliminarVendedor():

                  seleccion = listaVendedor_Modificar.selection()
                  if not seleccion:
                        messagebox.showwarning("Advertencia", "Debe seleccionar un Vendedor de la lista para eliminar")
                        return

                  with open(rutaLogin, "r") as archivo:
                        usuarios = json.load(archivo)

                  respuesta = messagebox.askquestion("Confirmar", "¿Está seguro que desea eliminar este Vendedor?")
                  if respuesta == "yes":
                        item_seleccionado = listaVendedor_Modificar.focus()
                        idSeleccionado = listaVendedor_Modificar.item(item_seleccionado, "text")
                        
                        if idSeleccionado in usuarios["Vendedor"]:
                              del usuarios["Vendedor"][idSeleccionado]
                              
                              with open(rutaLogin, "w") as archivo:
                                    json.dump(usuarios, archivo, indent=4)
                              
                              actualizarListaVendedor()
                              messagebox.showinfo("Éxito", "Vendedor eliminado correctamente")
                        else:
                              messagebox.showerror("Error", "El Vendedor seleccionado no existe")
                  else:
                        ventana_Administrador.focus_force()

            def volver():
                  actualizarVendedor()
                  ventanaListaVendedor.withdraw()
                  ventana_Administrador.deiconify()

            ventana_Administrador.withdraw()

            ventanaListaVendedor = Tk()
            ventanaListaVendedor.title("Lista de Vendedor")

            cuadrotreeviewModificar = LabelFrame(ventanaListaVendedor)
            cuadrotreeviewModificar.pack(ipadx= 5, ipady= 5, fill='both')

            listaVendedor_Modificar = ttk.Treeview(cuadrotreeviewModificar, columns=("Nombre", "Apellido", "Contraseña", "DNI", "Direccion","Telefono"))
            listaVendedor_Modificar.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both', side=LEFT, expand= True)
            listaVendedor_Modificar.heading("#0", text="ID")
            listaVendedor_Modificar.heading("#1", text="Nombre")
            listaVendedor_Modificar.heading("#2", text="Apellido")
            listaVendedor_Modificar.heading("#3", text="Contraseña")
            listaVendedor_Modificar.heading("#4", text="DNI")
            listaVendedor_Modificar.heading("#5", text="Direccion")
            listaVendedor_Modificar.heading("#6", text="Telefono")
            listaVendedor_Modificar.column("#0", width=30)
            listaVendedor_Modificar.column("#1", width=100)
            listaVendedor_Modificar.column("#2", width=100)
            listaVendedor_Modificar.column("#3", width=70)
            listaVendedor_Modificar.column("#4", width=100)
            listaVendedor_Modificar.column("#5", width=200)
            listaVendedor_Modificar.column("#6", width=100)

            cuadroBotonesModificar = LabelFrame(ventanaListaVendedor)
            cuadroBotonesModificar.pack(ipadx= 5, ipady= 5, fill='both')

            botonAñadir = Button(cuadroBotonesModificar, text="Añadir Vendedor", command=botonAñadirVendedor)
            botonAñadir.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both', side=LEFT, expand= True)

            botonModificar = Button(cuadroBotonesModificar, text="Modificar Vendedor", command= modificar_NuevoVendedor)
            botonModificar.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both', side=LEFT, expand= True)

            botonEliminar = Button(cuadroBotonesModificar, text="Eliminar Vendedor", command=eliminarVendedor)
            botonEliminar.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both', side=LEFT, expand= True)

            botonVolver = Button(cuadroBotonesModificar, text="Volver", command=volver)
            botonVolver.pack(ipadx= 30, ipady= 5, padx= 5, pady= 5, fill='both', side=LEFT, expand= True)

            if "Vendedor" in usuarios:
                  for vendedor, codigo in usuarios["Vendedor"].items():
                        listaVendedor_Modificar.insert("", "end", text= f"{vendedor}", values=(codigo["Nombre"], codigo["Apellido"], codigo["Contrasena"], codigo["DNI"], codigo["Direccion"], codigo["Telefono"]))
            
            actualizarListaVendedor()

            ventanaListaVendedor.mainloop()

      def etiqueta_tooltip(event):
            item_id = listaVendedor.identify_row(event.y)
            if item_id:
                  vendedor = listaVendedor.item(item_id, 'text')
                  for vendedorClave0, vendedorValor0 in usuarios["Vendedor"].items():
                        if vendedorClave0 == vendedor:
                              detalles = f"Nombre: {vendedorValor0['Nombre']}\nApellido: {vendedorValor0['Apellido']}\nTelefono: {vendedorValor0['Telefono']}"
                              etiquetaTooltip_Texto.config(text=detalles)
                              etiquetaTooltip_Texto.place(x=event.x_root - ventana_Administrador.winfo_rootx(), y=event.y_root - ventana_Administrador.winfo_rooty() + 20)
                              return
            etiquetaTooltip_Texto.place_forget()

      def ocutar_etiquetaTooltip(event):
            etiquetaTooltip_Texto.place_forget()

      def generar_informe_ventas():
      # Función para generar el informe de ventas por vendedor
            informe_ventas = ""

            with open(rutaVentas, "r") as archivo:
                  registroVentas = json.load(archivo)

            for vendedor, detalles in registroVentas["Vendedor"].items():
                  informe_ventas += f"Vendedor: {vendedor}\n"
                  for numero, productos in detalles["Numero"].items():
                        for producto, detalles_producto in productos.items():
                              informe_ventas += f"    - Producto: {producto}\n"
                              informe_ventas += f"      Cantidad vendida: {detalles_producto['Cantidad']}\n"
                              informe_ventas += f"      Precio unitario: {detalles_producto['Precio']}\n"
                              informe_ventas += f"      Precio total: {detalles_producto['PrecioTotal']}\n"
                  informe_ventas += "\n"

            # Crear y mostrar la ventana emergente con el informe
            ventana_informe = Tk()
            ventana_informe.title("Informe de Ventas por Vendedor")

            informe_texto = Text(ventana_informe, wrap=WORD, height=20, width=80)
            informe_texto.pack(padx=10, pady=10)
            informe_texto.insert(END, informe_ventas)
            informe_texto.config(state=DISABLED)  # Para hacer el texto de solo lectura

            cerrar_button = Button(ventana_informe, text="Cerrar", command=ventana_informe.destroy)
            cerrar_button.pack(pady=10, padx=10, ipady=10, ipadx=10)

      ventana_Administrador = Tk()
      ventana_Administrador.title("Ventana Administrador Accesibilidades")

      cuadrotreeview = LabelFrame (ventana_Administrador, text= "STOCK")
      cuadrotreeview.pack(ipadx= 5, ipady= 5, pady= 5, fill='both', side=LEFT, expand= True)

      ventanaBotones = LabelFrame(cuadrotreeview, text="Accesibilidades: ")
      ventanaBotones.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both')

      agregar_Boton = Button(ventanaBotones, text="Agregar Producto", command=agregar_producto)
      agregar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side=LEFT, expand= True)

      modificar_Boton = Button(ventanaBotones, text="Modificar Producto", command=modificar_producto)
      modificar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side=LEFT, expand= True)

      eliminar_Boton = Button(ventanaBotones, text="Eliminar Producto", command=eliminar_producto)
      eliminar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side=LEFT, expand= True)

      botonProveedor = Button(ventanaBotones, text="Proveedor")
      botonProveedor.pack(ipadx= 30, ipady= 5, padx= 5, pady= 5, side=LEFT, expand= True)

      botonSalir = Button(ventanaBotones, text="Salir", command=salir)
      botonSalir.pack(ipadx= 40, ipady= 5, padx= 5, pady= 5, side=LEFT, expand= True)

      ventanaTreeview = LabelFrame(cuadrotreeview, text="Lista de Stock producto: ")
      ventanaTreeview.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both')

      listaStock = ttk.Treeview(ventanaTreeview, columns=("Categoria", "Producto", "Cantidad", "Precio"))
      listaStock.pack(ipadx= 200, ipady= 70, padx= 5, pady= 5, side= LEFT, fill='both', expand=True)
      listaStock.heading("#0", text="Categoría")
      listaStock.heading("#1", text="Producto")
      listaStock.heading("#2", text="Modelo")
      listaStock.heading("#3", text="Cantidad")
      listaStock.heading("#4", text="Precio")
      listaStock.column("#0", width=50)
      listaStock.column("#1", width=100)
      listaStock.column("#2", width=250)
      listaStock.column("#3", width=5)
      listaStock.column("#4", width=5)


      scrollbarStock = Scrollbar(ventanaTreeview, orient="vertical", command=listaStock.yview)
      scrollbarStock.pack(side=LEFT, fill="both")

      listaStock.config(yscrollcommand= scrollbarStock.set)

      for clave0, valor0 in stock.items():
            for clave1, valor1 in valor0.items():
                  for clave2, valor2 in valor1.items():
                        cargar = listaStock.insert("", "end", text= clave0, values=(clave1, clave2, valor2["Cantidad"], valor2["Precio"]))

      actualizarStock()

      cuadroTreeviewVendedor = LabelFrame(ventanaTreeview)
      cuadroTreeviewVendedor.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both', expand=True, side=RIGHT)

      listaVendedor = ttk.Treeview(cuadroTreeviewVendedor, columns=("Vendedor"))
      listaVendedor.heading("#0", text="ID")
      listaVendedor.heading("#1", text="Vendedor")
      listaVendedor.column("#0", width=100)
      listaVendedor.column("#1", width=100)
      listaVendedor.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, fill='both')

      if "Vendedor" in usuarios:
            for vendedorClave0, vendedorValor0 in usuarios["Vendedor"].items():
                  cargarVendedor = listaVendedor.insert("", "end", text=vendedorClave0, values=(vendedorValor0["Nombre"]))

      actualizarVendedor()

      etiquetaTooltip_Texto = Label(ventana_Administrador, text="", relief=SOLID, borderwidth=1)

      listaVendedor.bind("<Motion>", etiqueta_tooltip)
      listaVendedor.bind("<Leave>", ocutar_etiquetaTooltip)

      cuadroAccesoVendedor = LabelFrame(cuadroTreeviewVendedor)
      cuadroAccesoVendedor.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand=True)

      informe_Boton = Button(cuadroAccesoVendedor, text="Informe", command=generar_informe_ventas)
      informe_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand=True)

      modificar_Boton = Button(cuadroAccesoVendedor, text="Modificar Lista", command=modificarVendedor)
      modificar_Boton.pack(ipadx= 5, ipady= 5, padx= 5, pady= 5, side= LEFT, expand=True)

      ventana_Administrador.mainloop()