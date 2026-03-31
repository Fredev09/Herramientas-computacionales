import mysql.connector

class Estudiantes:

    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="prueba"
        )
        return conexion
    
    def guardar(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "INSERT INTO estudiantes(nombre, edad) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def listar(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "SELECT id, nombre, edad FROM estudiantes"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    
    def consulta(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "SELECT nombre, edad FROM estudiantes WHERE id = %s"
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    
    def modificar(self, datos):
        con =self.abrir()
        cursor = con.cursor()
        sql = "UPDATE estudiantes SET nombre = %s, edad = %s WHERE id = %s" 
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def eliminar(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "DELETE FROM estudiantes WHERE id = %s"
        cursor.execute(sql, datos)
        con.commit()
        con.close()
        
