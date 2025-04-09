from conexion import conectar

conn = conectar()
if conn:
    print("Conexión exitosa!")
    conn.close()
else:
    print("No se pudo conectar.")