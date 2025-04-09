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
def validar_usuarios(entry1,entry2,ventana):
    if not entry1.get() == "Ad":
        messagebox.showerror("Error", "Ingrese un usuario valido")
    elif not entry2.get() == "Alesito":
        messagebox.showerror("Error", "Contraseña invalida")
    else:
        messagebox.showinfo("Ingresandoooo.....", "Ingresando como Administrador")


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
           command=lambda: validar_usuarios(entry_usuario, entry_contraseña, ventana))\
        .grid(row=5, column=0, columnspan=2, pady=20)



ventana = creacion_ventana()
ventana_login(ventana)
ventana.mainloop()

"""
ola
"""