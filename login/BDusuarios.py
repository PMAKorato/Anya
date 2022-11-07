import sqlite3 as sql

def crearDB():
    conn = sql.connect("Usuarios.db")
    conn.commit()
    conn.close()

def crearTabla():
    conn = sql.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE usuarios (
        usuario text,
        contrasena text
    )"""
    )
    conn.commit()
    conn.close()

def crearUsuario(user, passw):
    conn = sql.connect("Usuarios.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO usuarios VALUES ('{user}','{passw}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()





if __name__== "__main__":
   # crearDB()
   # crearTabla()
   #crearUsuario('Korato','DrakeElric1@')
   crearUsuario('a','a')
   