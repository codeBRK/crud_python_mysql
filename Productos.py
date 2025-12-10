from Conexion import *

class Productos:

    def mostrarProductos():

        try: 

            conexion = CConexion.conexionDB()
            cursor = conexion.cursor()
            sql = "SELECT * FROM productos"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            conexion.commit()
            cursor.close()
            conexion.close()
            return resultados

        except mysql.connector.Error as error:
            print("Error al mostrar los productos: {}".format(error))

    def ingresarProductos(descripcion, precio, stock):

        try: 

            conexion = CConexion.conexionDB()
            cursor = conexion.cursor()
            sql = "INSERT INTO productos (descripcion, precio, stock) VALUES (%s, %s, %s)"
            valores = (descripcion, precio, stock)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Producto ingresado exitosamente")
            cursor.close()
            conexion.close()

        except mysql.connector.Error as error:
            print("Error al ingresar el producto: {}".format(error))

    def actualizarProductos(id_producto, descripcion, precio, stock):

        try: 

            conexion = CConexion.conexionDB()
            cursor = conexion.cursor()
            sql = "UPDATE productos SET descripcion=%s, precio=%s, stock=%s WHERE id_producto=%s"
            valores = (descripcion, precio, stock, id_producto)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Producto actualizado exitosamente")
            cursor.close()
            conexion.close()

        except mysql.connector.Error as error:
            print("Error al actualizar el producto: {}".format(error))

    def eliminarProductos(id_producto):

        try: 

            conexion = CConexion.conexionDB()
            cursor = conexion.cursor()
            sql = "DELETE from productos WHERE id_producto = %s"
            valores = (id_producto,)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Producto Eliminado exitosamente")
            cursor.close()
            conexion.close()

        except mysql.connector.Error as error:
            print("Error al Eliminar el producto: {}".format(error))

    def filtrarProductos(descripcion):

        try: 

            conexion = CConexion.conexionDB()
            cursor = conexion.cursor()
            sql = "SELECT * FROM productos WHERE descripcion LIKE %s"
            valores = (f"%{descripcion}%",)
            cursor.execute(sql, valores)
            resultados = cursor.fetchall()
            conexion.commit()
            cursor.close()
            conexion.close()
            return resultados

        except mysql.connector.Error as error:
            print("Error al Filtrar el producto: {}".format(error))
            return []