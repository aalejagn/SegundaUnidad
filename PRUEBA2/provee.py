from tkinter import Tk, Label,Button,Entry,Frame

ventana = Tk()
ventana.title("Catalogo de Ventanas")
ventana.geometry("620x480")

lblTitulo = Label(ventana, text = "Catalogo de Proveedores")
lblTitulo.place(x = 150, y = 1, width = 200, height = 20)

lblIdproveedor = Label(ventana, text="Id proveedor")
lblIdproveedor.place(x =20, y = 30, width = 200, height = 20)
txtIdproveedor = Entry(ventana, bg = "gold")
txtIdproveedor.place(x = 20, y = 50, width = 200, height = 20)

lblNombre = Label(ventana, text = "Nombre")
lblNombre.place(x = 20, y = 80, width = 200, height = 20)
txtNombre = Entry(ventana, bg = "gold")
txtNombre.place(x = 20, y = 100, width = 200, height = 20) 

lblTelefono = Label(ventana, text = "Telefono")
lblTelefono.place(x = 20, y = 130, width = 200, height = 20)
txtTelefono = Entry(ventana, bg ="gold")
txtTelefono.place(x = 20, y = 150, width = 200, height = 20)

lblContacto = Label(ventana, text = "Contacto")
lblContacto.place(x = 20, y = 180, width = 200, height = 20)
txtContacto = Entry(ventana, bg= "gold")
txtContacto.place(x = 20, y = 200, width = 200, height = 20)



ventana.mainloop()



