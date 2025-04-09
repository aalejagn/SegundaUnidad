from conexion import conectar
import os

def ver_usuarios(cursor):
    try:
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        if resultados:
            for fila in resultados:
                print(fila)
        else:
            print("No hay usuarios registrados.")
    except mysql.connector.Error as e:
        print(f"Error al obtener los usuarios: {e}")

def pedir_datos():
    usuario = input("Ingresa el Id del usuario: ").strip()
    clave = input("Ingresa la clave del usuario: ").strip()
    return usuario, clave

def inserta_usuario(cursor, conexion, usuario, clave):
    try:
        query = "INSERT INTO usuarios(usuario, clave) VALUES (%s, MD5(%s))"
        valores = (usuario, clave)
        cursor.execute(query, valores)
        conexion.commit()
        print("Usuario insertado correctamente.")
    except mysql.connector.Error as e:
        print(f"Error al insertar usuario: {e}")

def actualiza_usuario(cursor, conexion, id, contra):
    try:
        query = "UPDATE usuarios SET clave = MD5(%s) WHERE usuario = %s"
        valores = (contra, id)
        cursor.execute(query, valores)
        conexion.commit()
        print("Clave actualizada correctamente.")
    except mysql.connector.Error as e:
        print(f"Error al actualizar clave: {e}")

def elimina_usuario(cursor, conexion, usuario):
    try:
        query = "DELETE FROM usuarios WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        conexion.commit()
        print("Usuario eliminado correctamente.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar usuario: {e}")

def cerrar_conexion(cursor, conexion):
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()
    print("Conexión cerrada.")

def menu():
    conexion = conectar()
    if not conexion:
        return

    cursor = conexion.cursor()

    while True:
        print("\nMenú")
        print("1. Ver usuarios")
        print("2. Insertar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        try:
            opc = int(input("Selecciona una opción: ").strip())
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        match opc:
            case 1:
                ver_usuarios(cursor)
            case 2:
                id, contra = pedir_datos()
                inserta_usuario(cursor, conexion, id, contra)
            case 3:
                id, contra = pedir_datos()
                actualiza_usuario(cursor, conexion, id, contra)
            case 4:
                id = input("Ingresa el Id del usuario a eliminar: ").strip()
                elimina_usuario(cursor, conexion, id)
            case 5:
                break
            case _:
                print("Opción no válida, intenta de nuevo.")

        os.system("pause")

    cerrar_conexion(cursor, conexion)

if __name__ == "__main__":
    menu()