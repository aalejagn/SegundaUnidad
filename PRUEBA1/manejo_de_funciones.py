from tkinter import Tk, Label,Frame, Entry, Button, ttk, messagebox
from db_soriana import ver_clientes
"""
Manejo de interfaz para cada entidad
"""
# # Manejo de la entidad de cliente frontend
def manejar_clientes(ventana, rol, barra_lateral):
    frame_clientes = Frame(ventana, bg="#E6F0FA")
    frame_clientes.pack(side="right", fill="both", expand=True)
    # # REGISTRAMOS LAS ENTRADAS
    entradas = {}
    filas = ["Telefono", "Nombre", "Dirección", "RFC", "Correo"]

    for i, fila in enumerate(filas):
        Label(frame_clientes, text=fila, bg="#E6F0FA").grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entrada = Entry(frame_clientes)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[fila] = entrada
        
    # # Creacion de framen para los botones para la funcion de clientes
    frame_botones = Frame(frame_clientes, bg = "#E6F0FA")
    frame_botones.grid(row=5, columnspan=2, pady=10)

    # # Creacion de tabla
    tabla = ttk.Treeview(frame_clientes, columns=("Teléfono", "Nombre", "Dirección", "RFC", "Correo"), show="headings")
    for col in ("Teléfono", "Nombre", "Dirección", "RFC", "Correo"):
        tabla.heading(col, text=col)
        tabla.column(col, width=100)
    tabla.grid(row=6, columnspan=2, pady=10, sticky="nsew")
    ver_clientes(tabla)
    return frame_clientes

# # # # Manejo de la entidad de cliente
def manejar_inventario():
    messagebox.showinfo("informando", "Hola que hace?")
    
# # Manejo de proveedores
def manejar_proveedor():
    messagebox.showinfo("informando", "Hola que hace?")
    
# # # Manejo de unidades
def manejar_unidades():
    messagebox.showinfo("informando", "Hola que hace?")
    
# # Manejo de categorias
def manejar_categorias():
    messagebox.showinfo("informando", "Hola que hace?")
    
# # # Manejo de metodo de pago
def manejar_metodo_pago():
    messagebox.showinfo("informando", "Hola que hace?")
    
# # Manejo de empleado
def manejar_empleado():
    messagebox.showinfo("informando", "Hola que hace?")
    