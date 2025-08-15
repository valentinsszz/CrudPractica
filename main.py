#Crud Para nombre y pais.
import pyodbc
import personas

def mostrarMenu():
    print("Eliga que opcion quiere, oprima 0 para salir")
    print("1 = Mostrar")
    print("2 = Agregar")
    print("3 = Editar")
    print("4 = Eliminar")

op = ""

while op !="0":
    mostrarMenu()
    op = input("Opción: ")

    if op == "1":
        print("Mostrando datos: ")
        opersona = personas.Persona()
        opersona.mostrar()
        
    elif op == "2":
        opersona = personas.Persona()
        print("Escriba el Nombre y Pais a Editar")
        Nombre = input()
        Pais = input()
        opersona.add(Nombre, Pais)
        
    elif op == "3":
        id = input("Cual desea editar indique su ID: ")
        Nombre = input("indique su nuevo Nombre: ")
        Pais = input("Indique su nuevo Pais: ")
        opersona = personas.Persona()
        opersona.update(Nombre, Pais, id)
    elif op == "4":
        print("Para eliminar una persona ponga su id")
        opersona = personas.Persona()
        id = str(input())
        opersona.delete(id)
    elif op == "0":
        print("Saliendo del programa...")
    else:
        print("Dato incorrecto")
        
    

