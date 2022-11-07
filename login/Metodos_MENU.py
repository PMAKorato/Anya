import DBalumnos as ADB
import sqlite3 as sql


def mostrar_menu(opciones):
    print('Seleccione una opcion:')
    for clave in sorted(opciones):
        print(f'{clave}) {opciones[clave][0]}')           

def leer_opcion(opciones):
    while (a := input('Opcion:')) not in opciones:
        print('Opcion incorrecta, vuelva a intentarlo')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones,opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion,opciones)
        print() # se imprime una linea en blanco para clarificar la salida en pantalla

def menu_principal():
    opciones = {
        '1':('Agregar Alumno', agregar),
        '2':('Listar Alumnos', listar),
        '3':('Eliminar Alumno', eliminar),
        '4':('Editar Alumno', editar),      
        '5':('Buscar Alumno', buscar),  
        '6':('Salir', salir)
    }       

    generar_menu(opciones,'6')



def agregar():
    Nombre = input('Ingrese el nombre del alumno: ')
    Apellido = input('Ingrese el apellido del alumno: ')
    Dni = input('Ingrese el dni del alumno: ')
    ADB.insertRow(Nombre,Apellido,Dni)
    print('Alumno agregado exitosamente')

    


def listar():
    print('Lista de Alumnos')
    print('DNI\tNombre\tApellido')
    ADB.listar()

    


def eliminar():
    DniD = input('Ingrese el dni del alumno que llevara con tacza: ')
    ADB.eliminar(DniD)
    print('Alumno enviado a la muerte :) pipipipi')



def salir():
    print('Saliendo del menu\n')



def editar():
    ADB.listar()
    ADB.editar()
    



def buscar():
    Nombre = input('Ingrese el nombre del alumno que desea buscar: ')
    ADB.search(Nombre)






if __name__== '__main__':
    menu_principal()








    


