import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",  # ¡Este es el parámetro correcto!
            user="root",
            password="Duoesme12@",
            database="dbsoriana",
            auth_plugin='mysql_native_password',
            port=3306
        )
        print("✅ Conexión exitosa a MySQL")
        return conexion
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
if __name__ == "__main__":
    # Solo se ejecuta al llamar directamente este archivo
    print("\n🔍 Probando conexión directamente...")
    conexion = conectar()
    if conexion:
        print("Prueba exitosa, cerrando conexión")
        conexion.close()