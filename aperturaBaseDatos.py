from mysql.connector import Error
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='ismael',
        db='pai2'
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
        infoServer = conexion.get_server_info()
        print("Info del servidor: {}".format(infoServer))
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
        print("Conectado a la base de datos: {}".format(row))
except Error as ex:
    print("Error durante la conexión: {}".format(ex))
