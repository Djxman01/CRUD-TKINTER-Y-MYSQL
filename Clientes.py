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


def modificarClientes(IdUsuario,nombres, apellidos, sexo):

        try: 
            cone = CConexion.ConexionBaseDeDatos()
            cursor= cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombres = %s, usuarios.apellidos = %s, usuarios.sexo = %sWhere usuarios.id = %s; "
            valores = (nombres,apellidos,sexo, IdUsuario)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro actualizado")
    
        except mysql.connector.Error as error: 
            print("Error de actualizacion de datos {}".format(error))


def eliminarClientes(IdUsuario):

        try: 
            cone = CConexion.ConexionBaseDeDatos()
            cursor= cone.cursor()
            sql = "DELETE from usuarios WHERE usuarios.id = %s;"
            valores = (IdUsuario,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close()
    
        except mysql.connector.Error as error: 
            print("Error de eliminacion de datos {}".format(error))