# test_db_connection.py
import mysql.connector
from mysql.connector import Error

def conectar():
    print("Attempting to connect to the database...")
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Duoesme12@",
            database="dbsoriana"
        )
        print("Database connection successful.")
        return conexion
    except Error as err:
        print(f"Error connecting to the database: {err}")
        return None

def test_query():
    conexion = conectar()
    if not conexion:
        print("Connection failed.")
        return

    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT telefono, nombre, direccion, rfc, correo, monedero_electronico FROM cliente")
        resultados = cursor.fetchall()
        print(f"Fetched {len(resultados)} rows:")
        for fila in resultados:
            print(fila)
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

if __name__ == "__main__":
    test_query()