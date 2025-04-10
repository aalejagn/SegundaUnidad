from tkinter import Tk, Label, Frame, Entry, Button, ttk, messagebox, StringVar
from db_sorianaa import ver_clientes  # Corregido el nombre del módulo
from manejo_de_funciones import *

"""
Funcion de creacion de ventana
"""
def creacion_ventana():
    ventana = Tk()
    ventana.title("Punto de venta - Soriana")
    ventana.geometry("800x600")
    ventana.configure(bg="#E6F0FA")  # Color de la ventana principal
    return ventana

"""
Creacion de presentacion
"""
def ventana_login(ventana):
    marco_sombra = Frame(ventana, bg="#80C4DE")
    marco_sombra.pack()

    marco_login = Frame(ventana, bg="white", padx=40, pady=40)
    marco_login.pack(pady=60)
    
    Label(marco_login, text="🛒 SORIANA", font=("Arial", 24, "bold"), fg="#1E90FF", bg="white")\
        .grid(row=0, column=0, columnspan=2, pady=(0,10))
    # 💠 SEPARADOR DECORATIVO
    ttk.Separator(marco_login, orient='horizontal')\
        .grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
       
    info = "Dirección: LAS GRANJAS AQUI MATAN\nCelular: +52 9613765449\nEmail: ag0013155@gmail.com"
    Label(marco_login, text=info, font=("Arial", 12), bg="white", justify="center")\
        .grid(row=2, column=0, columnspan=2, pady=(10))
    
    # # Creacion de usuario
    Label(marco_login, text="Ingrese el usuario:", font=("Arial", 12), bg="white")\
        .grid(row=3, column=0, sticky="e", pady=5, padx=5)
    tipo_usuario = StringVar()
    opciones = ttk.Combobox(marco_login, values=["Gerente", "Trabajador"], state="readonly", textvariable=tipo_usuario, font=("Arial",12))
    opciones.grid(row=3, column=1, pady=0, padx=10, ipadx=10, ipady=2)
    
    Label(marco_login, text="Ingrese la contraseña:", font=("Arial", 12), bg="white")\
        .grid(row=4, column=0, sticky="e", pady=5, padx=5)
    entry_contraseña = Entry(marco_login, font=("Arial", 12), show="*")
    entry_contraseña.grid(row=4, column=1, pady=0, padx=5, ipadx=18, ipady=2)
    
    Button(marco_login, text="Ingresar", font=("Arial", 13), width=15, 
           command=lambda: validar_usuarios(tipo_usuario, entry_contraseña, ventana, marco_login))\
        .grid(row=5, column=0, columnspan=2, pady=20)

"""
Creamos la funcion de validar datos para usuarios
"""
def validar_usuarios(opciones, entry_contraseña, ventana, marco_login):

    if opciones not in ["Gerente", "Trabajador"]:
        messagebox.showerror("Error", "Ingrese un usuario válido")
    elif entry_contraseña != "a":
        messagebox.showerror("Error", "Contraseña inválida")
    else:
        messagebox.showinfo("Ingresando...", f"Ingresando como {tipo_usuario}")
        marco_login.destroy()
        barra = barra_lateral(ventana, tipo_usuario)  # ← usuario es un string
        manejo_usuarios(ventana, tipo_usuario,barra)
    
"""
Creacion de lado lateral para los botones
"""

def barra_lateral(ventana, rol):
    barra_lateral = Frame(ventana, bg="#D3D3D3", width=200)
    barra_lateral.pack(side="left", fill="y")

    opciones = ["Clientes", "Inventario", "Proveedor", "Unidades", "Categorias", "Metodo de pago", "Empleado"]
    funciones = {
        "Clientes": lambda: manejo_usuarios(ventana, rol.get(), barra_lateral),
        "Inventario": lambda: manejar_inventario(ventana, barra_lateral),
        "Proveedor": lambda: manejar_proveedor(ventana, barra_lateral),
        "Unidades": lambda: manejar_unidades(ventana, barra_lateral),
        "Categorias": lambda: manejar_categorias(ventana, barra_lateral),
        "Metodo de pago": lambda: manejar_metodo_pago(ventana, barra_lateral),
        "Empleado": lambda: manejar_empleado(ventana, barra_lateral)
    }
    for opcion in opciones:
        Button(barra_lateral, text=opcion, bg="#4682B4", fg="white", width=20,
               font=("Arial", 12),
               command=funciones.get(opcion, lambda: None)).pack(pady=5, padx=10)

    # Frame secundario
    main_frame = Frame(ventana, bg="#6A5ACD")
    main_frame.pack(expand=True, fill="both")
    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#6A5ACD").pack(pady=20)
    Label(main_frame, text="Sistema Moderno y Eficiente", font=("Arial", 14), bg="#6A5ACD").pack(pady=10)

    caracteristicas = [
        "Rápido y fácil de usar",
        "Control de inventario en tiempo real",
        "Reportes detallados de ventas",
        "Gestión de clientes y proveedores"
    ]

    for i, texto in enumerate(caracteristicas):
        Label(main_frame, text="●", font=("Arial", 12), fg="#32CD32", bg="#6A5ACD").pack()
        Label(main_frame, text=texto, font=("Arial", 12), fg="white", bg="#6A5ACD").pack()

    Button(main_frame, text="¡COMENZAR AHORA!", font=("Arial", 14, "bold"), bg="#FFA500", fg="white",
           command=lambda: manejo_usuarios(ventana, rol.get(), barra_lateral)).pack(pady=30)

    return barra_lateral
if __name__ == "__main__":
    ventana = creacion_ventana()
    ventana_login(ventana)
    ventana.mainloop()

