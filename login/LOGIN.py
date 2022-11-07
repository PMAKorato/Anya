import sqlite3 as sql
import Metodos_MENU as me


def inicio():
    us = input('Usuario: ')
    ps = input('Contrasena: ')
    validarLogin(us,ps)

def validarLogin(us,ps):
    contador = 0 
    while True:
        conn = sql.connect("Usuarios.db")
        cursor = conn.cursor()
        usu = f"SELECT * FROM usuarios WHERE usuario = '{us}'"
        #contra = f"SELECT * FROM usuarios WHERE contrasena = '{ps}'"
        cursor.execute(usu)
        usuario = cursor.fetchall()
        conn.commit()
        conn.close()
        longitud = len(usuario)
        if longitud == 0:
            usuario = '??@@'
        if us == usuario[0][0] :
            if ps == usuario[0][1]:
                me.menu_principal()
                break
            else:
                contador = contador + 1
                print(f'Contraseña Incorrecta, le queda {2 - contador} intentos') 
                
                if contador == 2 :
                    print('Fallos los dos intentos')
                    inicio()
                    break
                ps = input('Ingrese nuevamente la Contraseña: ')
        else:
            print('El usuario no existe')
            inicio()
            break

inicio()


