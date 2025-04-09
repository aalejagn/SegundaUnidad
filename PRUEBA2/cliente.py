from tkinter import Tk, Label, Entry

# Crear ventana principal
ventana = Tk()
ventana.title("Catálogo de Clientes")
ventana.geometry("620x480")

# Título
lblTitulo = Label(ventana, text="Catálogo de Clientes", font=("Arial", 12, "bold"))
lblTitulo.place(x=150, y=10, width=300, height=20)

# Teléfono
Label(ventana, text="Teléfono").place(x=20, y=50, width=200, height=20)
txtTelefono = Entry(ventana, bg="gold")
txtTelefono.place(x=20, y=70, width=200, height=20)

# Nombre
Label(ventana, text="Nombre").place(x=20, y=100, width=200, height=20)
txtNombre = Entry(ventana, bg="gold")
txtNombre.place(x=20, y=120, width=200, height=20)

# RFC
Label(ventana, text="RFC").place(x=20, y=150, width=200, height=20)
txtRFC = Entry(ventana, bg="gold")
txtRFC.place(x=20, y=170, width=200, height=20)

# Dirección
Label(ventana, text="Dirección").place(x=20, y=200, width=200, height=20)
txtDireccion = Entry(ventana, bg="gold")
txtDireccion.place(x=20, y=220, width=200, height=20)

# Monedero Electrónico
Label(ventana, text="Monedero Electrónico").place(x=20, y=250, width=200, height=20)
txtMonedero = Entry(ventana, bg="gold")
txtMonedero.place(x=20, y=270, width=200, height=20)

ventana.mainloop()
