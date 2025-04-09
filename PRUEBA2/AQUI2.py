from tkinter import Tk, Label, Button, Entry, Frame
from tkinter import ttk

# Función para mostrar/ocultar la sección de usuarios
def toggle_usuarios():
    if frame_usuarios.winfo_ismapped():
        frame_usuarios.pack_forget()
    else:
        frame_usuarios.pack(pady=10)

# Crear ventana principal
root = Tk()
root.title("Sistema de Gestión")
root.geometry("700x600")

# Botón para mostrar/ocultar la sección de usuarios
Button(root, text="Usuarios", command=toggle_usuarios).pack(pady=10)

# Frame para la sección de usuarios
frame_usuarios = Frame(root)

Label(frame_usuarios, text="Teléfono:").grid(row=0, column=0)
Label(frame_usuarios, text="Nombre:").grid(row=1, column=0)
Label(frame_usuarios, text="Dirección:").grid(row=2, column=0)
Label(frame_usuarios, text="RFC:").grid(row=3, column=0)
Label(frame_usuarios, text="Correo:").grid(row=4, column=0)

telefono_entry = Entry(frame_usuarios)
nombre_entry = Entry(frame_usuarios)
direccion_entry = Entry(frame_usuarios)
rfc_entry = Entry(frame_usuarios)
correo_entry = Entry(frame_usuarios)

telefono_entry.grid(row=0, column=1)
nombre_entry.grid(row=1, column=1)
direccion_entry.grid(row=2, column=1)
rfc_entry.grid(row=3, column=1)
correo_entry.grid(row=4, column=1)

frame_buttons = Frame(frame_usuarios)
frame_buttons.grid(row=5, columnspan=2, pady=5)

Button(frame_buttons, text="Agregar").grid(row=0, column=0)
Button(frame_buttons, text="Eliminar").grid(row=0, column=1)
Button(frame_buttons, text="Actualizar").grid(row=1, column=0)
Button(frame_buttons, text="Limpiar Campos").grid(row=1, column=1)

# Tabla para mostrar clientes
tabla = ttk.Treeview(frame_usuarios, columns=("Telefono", "Nombre", "Direccion", "RFC", "Correo"), show="headings")
for col in ("Telefono", "Nombre", "Direccion", "RFC", "Correo"):
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.grid(row=6, columnspan=2, pady=10)

# Ejecutar aplicación
root.mainloop()
