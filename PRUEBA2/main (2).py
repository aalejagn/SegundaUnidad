from tkinter import Tk, Label, Entry

ventana = Tk()
ventana.title("Catálogo de Ventanas")
ventana.geometry("640x480")

lblTitulo = Label(ventana, text = "Catálogo de Categorías")
lblTitulo.place(x = 150, y = 1, width = 200, height = 20)

lblIdCategoria = Label(ventana, text = "IdCategorías")
lblIdCategoria.place(x = 20, y = 50, width = 100, height = 20)
txtIdCategoria = Entry(ventana, bg = "gold")
txtIdCategoria.place(x = 120, y = 50, width = 200, height = 20)

lblNombre = Label(ventana, text = "Nombre")
lblNombre.place(x = 20, y = 90, width = 100, height = 20)
txtNombre = Entry(ventana, bg = "#FFE6FF")
txtNombre.place(x = 120, y = 90, width = 200, height = 20)

ventana.mainloop()