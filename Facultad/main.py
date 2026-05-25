from classFacultad import Facultad
from classEstudiante import Estudiantes
from classCurso import Curso
from menu import mostrar_menu

def main(): 
    facultad = Facultad()

    while True:
        mostrar_menu()
        opcion = input("\nIngrese la opcion deseada: ")

        if opcion == "1": #Agregar miembro
                    while True:
                        nombre = input("Nombre: ")
                        if nombre == "":
                            print('El nombre no puede estar vacio')
                        else: 
                            break

                    while True:
                        apellido = input("Apellido: ")
                        if apellido == "":
                            print('El Apellido no puede estar vacio')
                        else: 
                            break

                    while True:
                        nroMat = input("Numero de Matricula: ")
                        if nroMat == "":
                            print("El numero de matricula no puede estar vacio")
                        elif not nroMat.isdigit():
                            print('El numero de matricula solo debe contener numeros')
                        else: 
                            nroMat_existe = False
                            for est in facultad.estudiantes:
                                if est.nroMat == nroMat:
                                    nroMat_existe = True
                            if nroMat_existe: 
                                print('El numero de matricula ingresado ya existe')
                            else:
                                break 

                        while True:
                            carrera = input("Carrera: ")
                            if carrera == "":
                                print("La carrera ingresada no existe")
                            else:
                                break
                        nuevoEstudiante = Estudiantes(nombre, apellido, nroMat, carrera)
                        facultad.agregar_estudiante(nuevoEstudiante)
                        print('Estudiante agregado correctamente.')
                        

        break
