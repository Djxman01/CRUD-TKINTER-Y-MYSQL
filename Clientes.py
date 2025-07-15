from Conexion import *
import mysql.connector




class CCLientes:

    def ingresarClientes(nombres, apellidos, sexo):

        try: 
            cone = CConexion.ConexionBaseDeDatos()
            cursor= cone.cursor()
            sql = "insert into usuarios values(null,%s,%s,%s);"
            # La variable valores tiene que ser una tupla
            valores = (nombres,apellidos,sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
    
        except mysql.connector.Error as error: 
            print("Error de deteccion de datos {}".format(error))


def mostrarClientes():
        try: 
            cone = CConexion.ConexionBaseDeDatos()
            cursor= cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
    
        except mysql.connector.Error as error: 
            print("Error al mostrar los datos {}".format(error))
