import sqlite3 as sql

def createDB():
    conn = sql.connect("Alumnos.db")
    conn.commit()
    conn.close()
    
def createTable():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE alumnos (
        nombre text,
        apellidos text,
        dni integer
        
    )"""
    )
    conn.commit()
    conn.close()
    
    
    
def insertRow(nombre, apellido, dni):
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO alumnos VALUES ('{nombre}','{apellido}',{dni})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
    
def readRow():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM alumnos"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
    
    
def insertRows(lista_alumnos):
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO alumnos VALUES (?,?,?)"
    cursor.executemany(instruccion,lista_alumnos)
    conn.commit()
    conn.close()
    
    
    
def readOrdered(parametro):
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM alumnos ORDER BY {parametro} " #DESC : Mayor a menor
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
    
def search(Nombre):
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM alumnos WHERE nombre = '{Nombre}'" #nombre like 'oren' :para ignorar mayusculas o minusculas nombre like 'oren%' : buscar dato que contega la palabra ojo: tambnien se puedo poner variable > < valor numerico y concatenar con ORDER BY 
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def updateFields():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE alumnos SET dni=00000 WHERE nombre like 'Anggie'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
def deleteRow():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM alumnos WHERE nombre='Anggie'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def editar():
    dni = input('Ingrese el dni: ')
    
    Nnew=input('Nuevo Nombre: ')
    Anew=input('Nuevo Apellido: ')
    Dnew=input('Nuevo dni: ')

    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE alumnos SET nombre = '{Nnew}', apellidos = '{Anew}',dni = '{Dnew}' WHERE dni ='{dni}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()    

def eliminar(dni):
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM alumnos WHERE dni='{dni}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()




def listar():
    conn = sql.connect("Alumnos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT nombre FROM alumnos"
    cursor.execute(instruccion)
    listan = cursor.fetchall()
    instruccion = f"SELECT apellidos FROM alumnos"
    cursor.execute(instruccion)
    listaa = cursor.fetchall()
    instruccion = f"SELECT dni FROM alumnos"
    cursor.execute(instruccion)
    listad = cursor.fetchall()
    conn.commit()
    conn.close()
    i = 0
    while i < len(listad):
        print(f'{listad[i][0]}\t{listan[i][0]}\t{listaa[i][0]}')       
        i +=1   
if __name__== "__main__":
   # createDB()
   #createTable()
   #insertRow("Oren","Arones",76208938)
   #insertRow("Anggie","Bravo",78521645)
   #readRow()
 #  listadealumons = [
 #      ("Anggie","Bravo",78521645),
 #      ("Piero","Nanquen",86842359)
 #  ]
   #insertRows(listadealumons)
   #readOrdered("nombre")
   #search()
   #updateFields()
   #deleteRow()
   #pass
   #listar()
   pass
