from tkinter import Tk, Label,Button,Entry,Frame


def mostrar_proveedores():
    """
    Funcion que muestra el catalogo de proveedores
    """
    frame_proveedores = Frame(ventana, bg = "white")
    frame_proveedores.pack(pady = 10)
    
    lblTitulo = Label(ventana, text = "Catalogo de Proveedores")
    lblTitulo.place(x = 150, y = 1, width = 200, height = 20)

    lblIdproveedor = Label(frame_proveedores, text="Id proveedor")
    lblIdproveedor.place(x =20, y = 30, width = 200, height = 20)
    txtIdproveedor = Entry(frame_proveedores, bg = "gold")
    txtIdproveedor.place(x = 20, y = 50, width = 200, height = 20)

    lblNombre = Label(frame_proveedores, text = "Nombre")
    lblNombre.place(x = 20, y = 80, width = 200, height = 20)
    txtNombre = Entry(frame_proveedores, bg = "gold")
    txtNombre.place(x = 20, y = 100, width = 200, height = 20) 

    lblTelefono = Label(frame_proveedores, text = "Telefono")
    lblTelefono.place(x = 20, y = 130, width = 200, height = 20)
    txtTelefono = Entry(frame_proveedores, bg ="gold")
    txtTelefono.place(x = 20, y = 150, width = 200, height = 20)

    lblContacto = Label(frame_proveedores, text = "Contacto")
    lblContacto.place(x = 20, y = 180, width = 200, height = 20)
    txtContacto = Entry(frame_proveedores, bg= "gold")
    txtContacto.place(x = 20, y = 200, width = 200, height = 20)
    
    

ventana = Tk()
ventana.title("Catalogo de Ventanas")
ventana.geometry("620x480")

bttonAbrir = Button(ventana, text = "Abrir Catalogo de Proveedroes", command = mostrar_proveedores)
bttonAbrir.pack(pady = 10)
ventana.mainloop()



