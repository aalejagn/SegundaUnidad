import mysql.connector 
from tkinter import messagebox
from conexion2 import conectar




"""
Funcion insertar, para clientes
"""
def insertar_cliente(telefono, nombre, direccion, rfc, correo):
    conexion = conectar()
    if not conexion:
        return False
    
    cursor = None
    
    try:
        if not telefono or not telefono:
            messagebox.showwarning("Advertencia", "Telfono y Nombre son campos obligatorios")
            return False
        
        cursor = conexion.cursor()
        consulta = """
        INSERT INTO cliente (telefono, nombre, direccion, rfc, correo)
        VALUES(%s,%s,%s,%s,%s)
        """    
        
        cursor.execute(consulta, (telefono, nombre,direccion,rfc,correo))
        conexion.commit()
        messagebox.showinfo("Exito", "Cliente insetado correctamente") 
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al insertar cliente: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()
 
"""
Funcion ver, para clientes
"""
def ver_clientes(tabla):
    conexion = conectar()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT telefono, nombre, direccion, rfc, correo FROM cliente")
        filas = cursor.fetchall()
        
    
        # # # # # Limpiar la tabla antes de actualizar
        for fila in tabla.get_children():
            tabla.delete(fila)
        
        # # Llenar la tabla con los datos
        for fila in filas:
            tabla.insert("","end", values = fila)
    except mysql.connector.Error as e:
        print(f"Error en la consulta: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()                   
            conexion.close()
 
""""
Fucnion para actualizar los datos de un cliente
"""
            
def actualizar_cliente(telefono, nombre, direccion, rfc,correo):
    conexion = conectar()     
    if not conexion:
        messagebox.showwarning("Advertencia", "Teléfono y Nombre son campos obligatorios")
        return False
    
    cursor = None
    try:
        if not telefono or not nombre:
            messagebox.showwarning("Advertencia", "Telefono y Nombre son campos obligatorios")
            return False
        
        cursor = conexion.cursor()
        consulta = """
        UPDATE cliente
        SET nombre = %s, direccion %s, rc = %s, correo = %s
        WHERE telefono = %s
        """

        cursor.execute(consulta,(nombre,direccion,rfc,correo,telefono))
        conexion.commit()
        messagebox.showinfo("Exito", "Cliente actualizado correctamente")
        return True
    except mysql.connector.Error as e:
        messagebox.showerror()
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()       

"""
Funcion para eliminar un cliente
"""

def eliminar_cliente(telefono):
    conexion = conectar()
    if not conexion:
        messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar")
        return False
    
    cursor = None
    try:
        if not telefono:
            messagebox.showwarning("Advertencia", "Selecione un cliente para eliminar")
            return False
        
        cursor = conexion.cursor()
        consulta = "DELETE FROM cliente WhHERE telefono = %s"
        cursor.execute(consulta,(telefono,))
        conexion.commit()
        messagebox.showinfo("Exito", "Cliente elimnado correctamente")
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al eliminar cliente: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def limpiar_campos(entradas):
    for entrada in entradas:
        entrada.delete(0,"end")         
        
        
        