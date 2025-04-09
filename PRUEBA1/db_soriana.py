# db_soriana.py
import mysql.connector
from tkinter import messagebox
from conexion2 import conectar

def insertar_cliente(telefono, nombre, direccion, rfc, correo):
    conexion = conectar()
    if not conexion:
        return False
    
    cursor = None
    try:
        if not telefono or not nombre:
            messagebox.showwarning("Advertencia", "Teléfono y Nombre son campos obligatorios")
            return False

        cursor = conexion.cursor()
        query = """
        INSERT INTO cliente (telefono, nombre, direccion, rfc, correo)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (telefono, nombre, direccion, rfc, correo))
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al insertar cliente: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def ver_clientes(tabla):  # Asegúrate de que este parámetro esté aquí
    conexion = conectar()
    if not conexion:
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT telefono, nombre, direccion, rfc, correo FROM cliente")
        rows = cursor.fetchall()
        
        # Limpiar la tabla antes de actualizar
        for row in tabla.get_children():
            tabla.delete(row)
        
        # Llenar la tabla con los datos
        for row in rows:
            tabla.insert("", "end", values=row)
    except mysql.connector.Error as e:
        print(f"Error en la consulta: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def actualizar_cliente(telefono, nombre, direccion, rfc, correo):
    conexion = conectar()
    if not conexion:
        return False
    
    cursor = None
    try:
        if not telefono or not nombre:
            messagebox.showwarning("Advertencia", "Teléfono y Nombre son campos obligatorios")
            return False

        cursor = conexion.cursor()
        query = """
        UPDATE cliente 
        SET nombre = %s, direccion = %s, rfc = %s, correo = %s
        WHERE telefono = %s
        """
        cursor.execute(query, (nombre, direccion, rfc, correo, telefono))
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al actualizar cliente: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def eliminar_cliente(telefono):
    conexion = conectar()
    if not conexion:
        return False
    
    cursor = None
    try:
        if not telefono:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar")
            return False

        cursor = conexion.cursor()
        query = "DELETE FROM cliente WHERE telefono = %s"
        cursor.execute(query, (telefono,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al eliminar cliente: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def limpiar_campos(entries):
    for entry in entries:
        entry.delete(0, "end")