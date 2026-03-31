import mysql.connector


class Articulos:

    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd1"
        )
        return conexion

    def alta(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def consulta(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "SELECT descripcion, precio FROM articulos WHERE codigo = %s"
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        con.close()
        return resultado

    def recuperar_todos(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "SELECT codigo, descripcion, precio FROM articulos"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    
    def modificar(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "UPDATE articulos SET descripcion = %s, precio = %s WHERE codigo = %s"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def eliminar(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "DELETE FROM articulos WHERE codigo = %s"
        cursor.execute(sql, datos)
        con.commit()
        con.close()