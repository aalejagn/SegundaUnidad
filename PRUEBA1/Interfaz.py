from tkinter import Tk, Label, Button, Entry, Frame, StringVar
from tkinter import ttk, messagebox
from db_sorianaa import insertar_cliente, actualizar_cliente,eliminar_cliente,ver_clientes,limpiar_campos


"""
Creamos la funcion de la ventana
"""
def crear_ventana():
    ventana = Tk()
    ventana.title("Punto de venta - SORIANA")
    ventana.geometry("800x600")
    ventana.configure(bg="#E6F0FA")
    return ventana

"""
Creamos la funcion para que el usuario
ingrese con el rol que le corresponde
"""
def seleccionar_usuario(ventana):
    frame_login = Frame(ventana, bg="#E6F0FA")
    frame_login.pack(expand=True)

    Label(frame_login, text="SORIANA", font=("Arial", 26, "bold"), fg="#1E90FF", bg="#E6F0FA").pack(pady=20)
    Label(frame_login, text="Direccion: Aun no se que poner\nCelular: +52 961 3765449\nEmail: ag0013155@gmail.com",
          font=("Arial", 8), bg="#E6F0FA").pack(pady=5)
    Label(frame_login, text="Software creado por el alumno Alejandro Gutierrez Nuñez", font=("Arial", 8), bg="#E6F0FA").pack(pady=5)

    Label(frame_login, text="Seleccione un tipo de usuario:", font=("Arial", 12), bg="#E6F0FA").pack(pady=20)
    tipo_usuario = StringVar()
    opciones = ttk.Combobox(frame_login, values=["Administrador", "Trabajador"], state="readonly", textvariable=tipo_usuario, font=("Arial", 12))
    opciones.pack(pady=10)

    Button(frame_login, text="Iniciar", font=("Arial", 12, "bold"), bg="#32CD32", fg="white",
           command=lambda: validar_usuario(tipo_usuario.get(), ventana, frame_login)).pack(pady=20)

"""
Validamos que ingrese por lo menos uno de los dos usuarios
"""
def validar_usuario(tipo_usuario, ventana, frame_login):
    if tipo_usuario in ["Administrador", "Trabajador"]:
        frame_login.destroy()
        crear_panel(ventana, tipo_usuario)
    else:
        messagebox.showerror("Error", "Por favor seleccione un tipo de usuario")

"""
Creamos la funcion de frame de los botones laterales
y de nuestro datos del software
"""
def crear_panel(ventana, rol):
    barra_lateral = Frame(ventana, bg="#D3D3D3", width=200)
    barra_lateral.pack(side="left", fill="y")

    opciones = ["INVENTARIO", "CLIENTES", "PROVEEDORES", "PEDIDOS", "REPORTE", "CONFIGURACION", "SALIDAS O GASTOS", "AUTOR"]
    for opcion in opciones:
        if opcion == "CLIENTES":
            Button(barra_lateral, text=opcion, font=("Arial", 12), bg="#4682B4", fg="white", width=20,
                   command=lambda: manejo_clientes(ventana, rol, barra_lateral)).pack(pady=5, padx=10)
        else:
            Button(barra_lateral, text=opcion, font=("Arial", 12), bg="#4682B4", fg="white", width=20).pack(pady=5, padx=10)

    main_frame = Frame(ventana, bg="#6A5ACD")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), fg="white", bg="#6A5ACD").pack(pady=20)
    Label(main_frame, text="Sistema moderno y eficiente", font=("Arial", 14), fg="white", bg="#6A5ACD").pack(pady=10)

    info_frame = Frame(main_frame, bg="#6A5ACD")
    info_frame.pack(pady=30)

    Label(info_frame, text="[Ventas]", font=("Arial", 12), fg="white", bg="#6A5ACD").grid(row=0, column=0, padx=40)
    Label(info_frame, text="[Reportes]", font=("Arial", 12), fg="white", bg="#6A5ACD").grid(row=0, column=1, padx=40)
    Label(info_frame, text="[Inventario]", font=("Arial", 12), fg="white", bg="#6A5ACD").grid(row=0, column=2, padx=40)

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
           command=lambda: contenido_principal(ventana, rol, barra_lateral)).pack(pady=30)


"""
Creamos una mini frame para el titulo de
punto de venta
"""
def contenido_principal(ventana, rol, barra_lateral):
    for contenido in ventana.winfo_children():
        if contenido != barra_lateral:
            contenido.destroy()

    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"Rol: {rol}", font=("Arial", 12), bg="#E6F0FA").pack()

"""
Manejamos los usuarios en este caso solo para usuario administrado
se le agrego las funciones en otro caso cuando se maneje el usuario de trabajador
se le agregar ciertas funciones
"""
def manejo_clientes(ventana, rol, barra_lateral):
    for contenido in ventana.winfo_children():
        if contenido != barra_lateral:
            contenido.destroy()

    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"Rol: {rol}", font=("Arial", 12), bg="#E6F0FA").pack()

    if rol == "Administrador":
        frame_clientes = crear_seccion_clientes(main_frame, rol)
    else:
        Label(main_frame, text="No tienes permiso para acceder a esta sección",
              font=("Arial", 12), bg="#E6F0FA").pack(pady=20)

"""
Manejo de otro frame para los datos de usuario
y para el uso de las funciones de db_soriana
"""

def crear_seccion_clientes(ventana, rol):
    # # # Creamos un frame para agregar los datos del cliente
    frame_cliente = Frame(ventana, bg = "#E6F0FA")

    # # Entradas de datos que usuario ingreara
    entradas = {}
    etiquetas = ["Telefono", "Nombre", "Dirección:", "RFC:", "Correo:"]
    for i, etiqueta in enumerate[etiquetas]:
        Label(frame_cliente, text = etiqueta, bg = "#E6F0FA").grid(row=i, column=0,padx=5, pady=5,sticky="e")
        entrada = Entry(frame_cliente)
        entrada.grid(row=i, column=1, padx=5, pady= 5)
        entradas[etiqueta] = entrada

    # Creacion de botones para la seccion de clientes
    frame_buttons = Frame(frame_cliente, bg = "#E6F0FA")
    frame_buttons.grid(row = 5, columnspan=2, pady=10)

    # # Creacion de la tabla con ttk.Treeview
    tabla = ttk.Treeview(frame_cliente, columns=("Telefono", "Nombre", "Dirección:", "RFC:", "Correo:"), show="headings")
    for col in ("Telefono", "Nombre", "Dirección:", "RFC:", "Correo:"):
        tabla.heading(col, text = col)
        tabla.column(col, width=100)
    tabla.grid(row=6, columnspan=2, pady=10, sticky="nsew")    

    # # observacion de los datos del cliente en la tabla creada
    ver_clientes(tabla)

    """
    Funcionamiento de los botones
    """

    def in_agregar():
        telefono = entradas["Telefono:"].get().strip()
        nombre = entradas["Nombre:"].get().strp()
        direccion = entradas["Direccion:"].get().strip()
        rfc = entradas["RFC:"].get().strip()
        correo = entradas["Correo:"].get().strip()

        if insertar_cliente(telefono,nombre,direccion,rfc,correo):
            ver_clientes(tabla)
            limpiar_campos(entradas.values())

if __name__ == "__main__":
    ventana = crear_ventana()
    seleccionar_usuario(ventana)
    ventana.mainloop()