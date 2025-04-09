from tkinter import Tk, Label,Frame, Entry, Button, ttk, messagebox
from db_sorianaa import insertar_cliente


"""
Funcion de creacion de ventana
"""

def creacion_ventana():
    ventana = Tk()
    ventana.title("Punto de venta -Soriana")
    ventana.geometry("800x600")
    ventana.configure(bg="#E6F0FA") #Color de la ventana principal
    return ventana

"""
Creacion de presentacion
"""
def ventana_login(ventana):
    login = Frame(ventana, bg="#E6F0FA")
    


ventana = creacion_ventana()
ventana.mainloop()
