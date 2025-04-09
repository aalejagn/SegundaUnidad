from tkinter import Tk, Label,Frame, Entry, Button, ttk, messagebox
from db_sorianaa import insertar_cliente


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
    marco_sombra.pack(pady=60)

    marco_login = Frame(ventana, bg="white", padx=40, pady=40)
    marco_login.pack()
    
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

def barra_lateral(ventana,rol):
    barra_lateral = Frame(ventana, bg="#D3D3D3", width=200)
    barra_lateral.pack(side="left", fill= "y")

    opciones = ["Inventario", "Clientes", "Proveedor", "Pedidos", "Reportes", "Configuración", "Gastos", "Informacion"]
    for opcion in opciones:
        if opcion == "Cliente":
            Button(barra_lateral, text = opcion, bg = "#4682B4", fg = "white", width=20,
                   command= lambda: manejar_clientes(ventana,rol,barra_lateral)).pack(pady=5,padx=10)
        else:
            Button(barra_lateral, text=opcion, font=("Arial",12), bg = "#4682B4", fg = "white", width = 20)

        if opcion == "Inventario":
            break
        if opcion == "Proveedor":
            break
        if opcion == "Pedidos":
            break
        if opcion == "Reportes":
            break
        if opcion == "Configuracion":
            break
        if opcion == "Informacion":
            break

def manejar_clientes(ventana,rol,barra_lateral):
    pass





ventana = creacion_ventana()
ventana_login(ventana)
ventana.mainloop()

