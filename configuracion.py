import json

rutaLogin = "C:/Users/rokha/Desktop/inteProg/usuarios.json"
rutaStock = "C:/Users/rokha/Desktop/inteProg/productos.json"

def cargarUsuarios():
    with open (rutaLogin, "r") as archivo:
        return json.load(archivo)
    
    
def cargarStock():
    with open (rutaStock, "r") as archivo: 
        return json.load(archivo)
    
def guardarStock(nuevoStock):
    with open (rutaStock, "w") as archivo:
        json.dump(nuevoStock, archivo, ident = 4)