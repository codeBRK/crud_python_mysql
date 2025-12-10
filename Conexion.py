#conexion a nuestra base de datos por medio del comando: python -m pip install mysql-connector-python

import mysql.connector

class CConexion:
    def conexionDB():
        try:
            conexion = mysql.connector.connect(
                user="root",
                password="Br@yan00",
                host="127.0.0.1",
                database="ferreteriadb",
                port="3306")
            print("Conexion exitosa")
            return conexion
        
        except mysql.connector.Error as error: 
            print("Error al conectar a la base de datos: {}".format(error))

            return conexion
        
    conexionDB()