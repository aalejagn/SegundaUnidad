import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Duoesme12@",
            database="db_soriana",
            port=3306  
        )
        return conexion
    except Error as err:
        messagebox.showerror("Error", f"No se pudo conectar a MySQL:\n{err}")
        return None