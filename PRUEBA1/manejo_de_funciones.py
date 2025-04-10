from tkinter import Tk, Label,Frame, Entry, Button, ttk, messagebox
from db_soriana import ver_clientes
"""
Manejo de interfaz para cada entidad
"""
def manejo_usuarios(ventana,rol,barra_lateral):
    for widget in ventana.winfo_children():
        if widget != barra_lateral:
            widget.destroy

    main_frame = Frame(ventana, bg = "#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUTNO DE VENTA", font=("Arial", 20, "bold"), bg = "#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"Rol{rol}", font=("Arial", 12), bg="#E6F0FA").pack()

    if rol == "Ad":
        frame_clientes = crear_seccion_clientes(main_frame,rol)
        frame_clientes.pack(pady=10)
    else:
        Label(main_frame, text = "Acceso restringido: Solo Administradores pueden gestionar clientes.",
              font= ("Arial", 12), bg = "#E6F0FA").pack(pady=10)

# # Manejo de la entidad de cliente frontend
def crear_seccion_clientes(ventana, rol):
    frame_clientes = Frame(ventana, bg="#E6F0FA")
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
    