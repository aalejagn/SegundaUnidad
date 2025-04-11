from tkinter import Tk, Label, Frame, Entry, Button, ttk, messagebox
from db_sorianaa import *

"""
Manejo de interfaz para cada entidad
"""
def manejo_usuarios(ventana,tipo_usuario, barra_lateral):
    for widget in ventana.winfo_children():
        if widget != barra_lateral:
            widget.destroy()

    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"tipo_usuario: {tipo_usuario}", font=("Arial", 12), bg="#E6F0FA").pack()

    if tipo_usuario in ["Gerente"]:
        frame_clientes = crear_seccion_clientes(main_frame, tipo_usuario)
        frame_clientes.pack(pady=10)
    else:
        Label(main_frame, text="Acceso restringido: Solo Administradores pueden gestionar clientes.",
              font=("Arial", 12), bg="#E6F0FA").pack(pady=10)

# Manejo de la entidad de cliente frontend
def crear_seccion_clientes(ventana, tipo_usuario):
    frame_clientes = Frame(ventana, bg="#E6F0FA")
    # REGISTRAMOS LAS ENTRADAS
    entradas = {}
    filas = ["Telefono:", "Nombre:", "Dirección:", "RFC:", "Correo:"]

    for i, fila in enumerate(filas):
        Label(frame_clientes, text=fila, bg="#E6F0FA").grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entrada = Entry(frame_clientes)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[fila] = entrada
        
    # Creacion de frame para los botones para la funcion de clientes
    frame_botones = Frame(frame_clientes, bg="#E6F0FA")
    frame_botones.grid(row=5, columnspan=2, pady=10)

    # Creacion de tabla
    tabla = ttk.Treeview(frame_clientes, columns=("Teléfono", "Nombre", "Dirección", "RFC", "Correo"), show="headings")
    for col in ("Teléfono", "Nombre", "Dirección", "RFC", "Correo"):
        tabla.heading(col, text=col)
        tabla.column(col, width=100)
    tabla.grid(row=6, columnspan=2, pady=10, sticky="nsew")
    ver_clientes(tabla)

    return frame_clientes

# Manejo de la entidad de inventario
def manejar_inventario(ventana, barra_lateral):

    pass
# Manejo de proveedores
def manejar_proveedor(ventana, barra_lateral):
    pass
# Manejo de unidades
def manejar_unidades(ventana, barra_lateral):
    pass
# Manejo de categorias
def manejar_categorias(ventana, barra_lateral):
    pass
# Manejo de metodo de pago
def manejar_metodo_pago(ventana, barra_lateral):
    pass
# Manejo de empleado
def manejar_empleado(ventana, barra_lateral):
    pass