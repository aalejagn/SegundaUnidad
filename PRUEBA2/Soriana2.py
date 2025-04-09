import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Configuración de la conexión a la base de datos
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Duoesme12@",
            database="dbsoriana",
            port = "3306"
        )
        return conexion
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a la BD: {e}")
        return None

# Función para insertar usuario
def insertar_usuario():
    usuario = entry_usuario.get().strip()
    clave = entry_clave.get().strip()

    if not usuario or not clave:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return

    conexion = conectar_bd()
    if not conexion:
        return

    cursor = conexion.cursor()
    try:
        query = "INSERT INTO usuarios(usuario, clave) VALUES (%s, MD5(%s))"
        cursor.execute(query, (usuario, clave))
        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario insertado correctamente.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo insertar usuario: {e}")
    finally:
        cursor.close()
        conexion.close()

# Función para ver usuarios
def ver_usuarios():
    conexion = conectar_bd()
    if not conexion:
        return

    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        lista_usuarios.delete(0, tk.END)
        for fila in resultados:
            lista_usuarios.insert(tk.END, fila)
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron obtener los usuarios: {e}")
    finally:
        cursor.close()
        conexion.close()

# Función para actualizar usuario
def actualizar_usuario():
    usuario = entry_usuario.get().strip()
    clave = entry_clave.get().strip()

    if not usuario or not clave:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return

    conexion = conectar_bd()
    if not conexion:
        return

    cursor = conexion.cursor()
    try:
        query = "UPDATE usuarios SET clave = MD5(%s) WHERE usuario = %s"
        cursor.execute(query, (clave, usuario))
        conexion.commit()
        messagebox.showinfo("Éxito", "Clave actualizada correctamente.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
    finally:
        cursor.close()
        conexion.close()

# Función para eliminar usuario
def eliminar_usuario():
    usuario = entry_usuario.get().strip()

    if not usuario:
        messagebox.showwarning("Advertencia", "Ingresa el ID del usuario a eliminar.")
        return

    conexion = conectar_bd()
    if not conexion:
        return

    cursor = conexion.cursor()
    try:
        query = "DELETE FROM usuarios WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo eliminar: {e}")
    finally:
        cursor.close()
        conexion.close()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Gestión de Usuarios")
ventana.geometry("400x400")

# Campos de entrada
tk.Label(ventana, text="Usuario:").pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

tk.Label(ventana, text="Clave:").pack()
entry_clave = tk.Entry(ventana, show="*")
entry_clave.pack()

# Botones
tk.Button(ventana, text="Ver Usuarios", command=ver_usuarios).pack()
tk.Button(ventana, text="Insertar Usuario", command=insertar_usuario).pack()
tk.Button(ventana, text="Actualizar Clave", command=actualizar_usuario).pack()
tk.Button(ventana, text="Eliminar Usuario", command=eliminar_usuario).pack()

# Lista de usuarios
lista_usuarios = tk.Listbox(ventana, width=50, height=10)
lista_usuarios.pack()

# Ejecutar la ventana
ventana.mainloop()