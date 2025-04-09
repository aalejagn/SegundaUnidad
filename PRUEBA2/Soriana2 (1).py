from conexion import conectar
import tkinter as tk
from tkinter import messagebox

# Función para insertar usuario
def insertar_usuario():
    try:
        id_usuario = int(entry_usuario.get().strip())  # Asegurarse de que sea un número
        nombre = entry_nombre.get().strip()

        if not nombre:
            messagebox.showwarning("Advertencia", "El campo nombre es obligatorio.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        query = "INSERT INTO usuario (id_usuario, nombre) VALUES (%s, %s)"
        cursor.execute(query, (id_usuario, nombre))
        conexion.commit()

        messagebox.showinfo("Éxito", "Usuario insertado correctamente.")
        ver_usuarios()  # Actualiza la lista
    except ValueError:
        messagebox.showerror("Error", "El ID de usuario debe ser un número.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo insertar usuario: {e}")
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()

# Función para ver usuarios
def ver_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM usuario")
        resultados = cursor.fetchall()
        lista_usuarios.delete(0, tk.END)
        for fila in resultados:
            lista_usuarios.insert(tk.END, f"ID: {fila[0]} - Nombre: {fila[1]}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los usuarios: {e}")
    finally:
        cursor.close()
        conexion.close()

# Función para actualizar usuario
def actualizar_usuario():
    try:
        id_usuario = int(entry_usuario.get().strip())
        nombre = entry_nombre.get().strip()

        if not nombre:
            messagebox.showwarning("Advertencia", "El campo nombre es obligatorio.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        query = "UPDATE usuario SET nombre = %s WHERE id_usuario = %s"
        cursor.execute(query, (nombre, id_usuario))
        conexion.commit()

        messagebox.showinfo("Éxito", "Nombre actualizado correctamente.")
        ver_usuarios()
    except ValueError:
        messagebox.showerror("Error", "El ID de usuario debe ser un número.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
    finally:
        cursor.close()
        conexion.close()

# Función para eliminar usuario
def eliminar_usuario():
    try:
        id_usuario = int(entry_usuario.get().strip())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "DELETE FROM usuario WHERE id_usuario = %s"
        cursor.execute(query, (id_usuario,))
        conexion.commit()

        messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
        ver_usuarios()
    except ValueError:
        messagebox.showerror("Error", "El ID de usuario debe ser un número.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar: {e}")
    finally:
        cursor.close()
        conexion.close()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Gestión de Usuarios")
ventana.geometry("400x400")

# Campos de entrada
tk.Label(ventana, text="ID Usuario:").pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Botones
tk.Button(ventana, text="Ver Usuarios", command=ver_usuarios).pack()
tk.Button(ventana, text="Insertar Usuario", command=insertar_usuario).pack()
tk.Button(ventana, text="Actualizar Usuario", command=actualizar_usuario).pack()
tk.Button(ventana, text="Eliminar Usuario", command=eliminar_usuario).pack()

# Lista de usuarios
lista_usuarios = tk.Listbox(ventana, width=50, height=10)
lista_usuarios.pack()

# Cargar usuarios al iniciar
ver_usuarios()

# Ejecutar la ventana
ventana.mainloop()
