import mysql.connector
from mysql.connector import Error

def connection(): #FUNCION PARA HACER CONEXION A BASE DE DATOS
    """
        Conexion db replicacion
    """
    connect = mysql.connector.connect(host="192.168.100.30", port="3306", user="root", passwd="root", db="asteriskcdrdb")
    cursor = connect.cursor(dictionary=False)
    try:
        if connect.is_connected():
            cursor.execute("select database();")
            record = cursor.fetchone()
            return connect, cursor
    except Error as e:
        return {"Error: ", e}


def connectionMZ(): #FUNCION PARA HACER CONEXION A BASE DE DATOS
    """
        Conexion db mazatlan
    """
    connect = mysql.connector.connect(host="192.168.100.29", port="3306", user="root", passwd="root", db="asteriskcdrdb")
    cursor = connect.cursor(dictionary=False)
    try:
        if connect.is_connected():
            cursor.execute("select database();")
            record = cursor.fetchone()
            return connect, cursor
    except Error as e:
        return {"Error: ", e}


def disconnection(connect, cursor):
    try:
        if connect.is_connected():
            if cursor.with_rows:
                cursor.fetchall()

            cursor.close()

            connect.commit()

            connect.close()

            return {"success": "MySQL connection is closed"}

    except mysql.connector.Error as e:
        return {"Error: ", e}

