from tkinter import Tk, Label,Frame, Entry, Button, ttk, messagebox
from db_sorianaa import ver_clientes
from manejo_de_funciones import *

"""
Funcion de creacion de ventana
"""
def creacion_ventana():
    ventana = Tk()
    ventana.title("Punto de venta -Soriana")
    ventana.geometry("800x600")
    ventana.configure(bg = "#E6F0FA") #Color de la ventana principal
    return ventana

"""
Creamos la funcion de validar datos para usuarios
"""
def validar_usuarios(entry_usuario,entry_contraseña,ventana,marco_login):
    if entry_usuario.get() not in ["Ad", "Trabajador"]:
        messagebox.showerror("Error", "Ingrese un usuario valido")
    if not entry_contraseña.get() == "a":
        messagebox.showerror("Error", "Contraseña invalida")
    else:
        messagebox.showinfo("Ingresandoooo.....", "Ingresando como Administrador")
        if entry_usuario.get() in ["Ad", "Trabajador"]:
            marco_login.destroy()
            barra_lateral(ventana, entry_usuario)

"""
Creacion de presentacion
"""
def ventana_login(ventana):
    marco_sombra = Frame(ventana,bg = "#80C4DE")
    marco_sombra.pack()

    marco_login = Frame(ventana, bg="white", padx=40, pady=40)
    marco_login.pack(pady=60)
    
    Label(marco_login, text="🛒 SORIANA", font=("Arial", 24, "bold"), fg="#1E90FF", bg = "white")\
        .grid(row=0, column=0, columnspan=2, pady=(0,10))
    # 💠 SEPARADOR DECORATIVO
    ttk.Separator(marco_login, orient='horizontal')\
        .grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
       
    info = "Dirección: LAS GRANJAS AQUI MATAN\nCelular: +52 9613765449\nEmail: ag0013155@gmail.com"
    Label(marco_login, text=info, font=("Arial", 12), bg = "white", justify="center")\
        .grid(row=2, column=0, columnspan=2, pady=(10))
    Label(marco_login, text="Ingrese el usuario:", font=("Arial", 12), bg = "white")\
        .grid(row=3, column=0, sticky="e", pady=5, padx=5)
    entry_usuario = Entry(marco_login, font=("Arial", 12))
    entry_usuario.grid(row=3, column=1, pady=5, padx=5, ipadx=10,ipady=5)
    
    Label(marco_login, text="Ingrese la contraseña:", font=("Arial", 12), bg = "white")\
        .grid(row=4, column=0, sticky="e", pady=5, padx=5)
    entry_contraseña = Entry(marco_login, font=("Arial", 12), show="*")
    entry_contraseña.grid(row=4, column=1, pady=5, padx=5, ipadx=10,ipady=5)
    
    Button(marco_login, text="Ingresar", font=("Arial", 13), width=15, 
           command=lambda: validar_usuarios(entry_usuario, entry_contraseña, ventana,marco_login))\
        .grid(row=5, column=0, columnspan=2, pady=20)


    opciones = ["Inventario", "Clientes", "Proveedor", "Pedidos", "Reportes", "Configuración", "Gastos", "Informacion"]

"""
Creacion de lado lateral para los botones
"""

def barra_lateral(ventana, rol):
    barra_lateral = Frame(ventana, bg="#D3D3D3", width=200)
    barra_lateral.pack(side="left", fill="y")

    opciones = ["Clientes","Inventario", "Proveedor", "Unidades", "Categorias", "Metodo de pago", "Empleado"]
    funciones = {
        "Clientes": crear_seccion_clientes(ventana, rol),
        "Inventario": manejar_inventario,
        "Proveedor": manejar_proveedor,
        "Unidades": manejar_unidades,
        "Categorias": manejar_categorias,
        "Metodo de pago": manejar_metodo_pago,
        "Empleado": manejar_empleado
    }
    for opcion in opciones:
            Button(barra_lateral, text=opcion, bg="#4682B4", fg="white", width=20,
                   font=("Arial", 12),
                   command=funciones.get(opcion, lambda: None)).pack(pady=5, padx=10)

def mostrar_conenido_principal(ventana,rol,barra_lateral):
    for widget in ventana.winfo_children():
        if widget != barra_lateral:
            widget.destroy()
    
    main_frame = Frame(ventana, bg = "#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA",)
    Label(main_frame, text=f"Rol, {rol}", font=("Arial", 12), bg = "#E6F0FA").pack()
    frame_clientess = crear_seccion_clientes(main_frame,rol)
    frame_clientess.pack(pady=10)

ventana = creacion_ventana()
ventana_login(ventana)
ventana.mainloop()

