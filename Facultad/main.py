from classFacultad import Facultad
from classEstudiante import Estudiantes
from classCurso import Curso
from menu import mostrar_menu

def main(): 
    facultad = Facultad(500)

    while True:
        mostrar_menu()
        opcion = input("\nIngrese la opcion deseada: ").strip()

        if opcion == "1": # Agregar Estudiante
            while True:
                nombre = input("Nombre: ").strip()
                if nombre == "":
                    print('El nombre no puede estar vacio')
                elif not nombre.replace(" ", "").isalpha():
                    print('El nombre solo debe contener letras')
                else: 
                    break

            while True:
                apellido = input("Apellido: ").strip()
                if apellido == "":
                    print('El Apellido no puede estar vacio')
                elif not apellido.replace(" ", "").isalpha():
                    print('El apellido solo debe contener letras')
                else: 
                    break

            while True:
                nroMat = input("Numero de Matricula: ").strip()
                if nroMat == "":
                    print("El numero de matricula no puede estar vacio")
                elif not nroMat.isdigit():
                    print('El numero de matricula solo debe contener numeros')
                else: 
                    nroMat_existe = False
                    for est in facultad.estudiantes:
                        if est.nroMat == nroMat:
                            nroMat_existe = True
                            break
                    if nroMat_existe: 
                        print('El numero de matricula ingresado ya existe')
                    else:
                        break 

            while True:
                carrera = input("Carrera: ").strip()
                if carrera == "":
                    print("La carrera no puede estar vacia")
                elif not carrera.replace(" ", "").isalpha():
                    print('La carrera solo debe contener letras')
                else:
                    break
                    
            nuevoEstudiante = Estudiantes(nombre, apellido, nroMat, carrera)
            facultad.agregar_estudiante(nuevoEstudiante)
            print('Estudiante agregado correctamente.')

        elif opcion == "2": # Agregar Curso
            while True:
                nomCurso = input("Nombre del curso: ").strip()
                if nomCurso == "":
                    print('El nombre del curso no puede estar vacio')
                elif nomCurso.isdigit():
                    print('El nombre del curso no puede ser únicamente un número ')
                else:
                    break

            while True:
                codCurso = input("Codigo del Curso: ").strip()
                if codCurso == "":
                    print("El Codigo del curso no puede estar vacio")
                elif not codCurso.isdigit():
                    print('El Codigo del curso solo debe contener numeros')
                else: 
                    codCurso_existe = False
                    for curso in facultad.cursos:
                        if curso.codCurso == codCurso:
                            codCurso_existe = True
                            break
                    if codCurso_existe: 
                        print('El Codigo de curso ingresado ya existe')
                    else:
                        break 

            while True:
                profEncargado = input("Profesor Encargado: ").strip()
                if profEncargado == "":
                    print('El Profesor Encargado no puede estar vacio')
                elif not profEncargado.replace(" ", "").isalpha():
                    print('El nombre del profesor solo debe contener letras')
                else:
                    break

            while True:
                capacidadMaxima = input("Capacidad Maxima de Alumnos en el curso: ").strip()
                if capacidadMaxima == "":
                    print('La capacidad maxima no puede estar vacia')
                elif not capacidadMaxima.isdigit(): 
                    print('La capacidad maxima solo debe contener numeros')
                else: 
                    break
                    
            nuevo_curso = Curso(nomCurso, codCurso, profEncargado, capacidadMaxima)
            facultad.agregar_curso(nuevo_curso)
            print('Curso agregado correctamente.')

        elif opcion == "3": # Inscribirse a un curso
            if not facultad.estudiantes or not facultad.cursos:
                print("No se pueden realizar inscripciones porque faltan registrar estudiantes o cursos.")
                continue
                
            estudiante = facultad.buscar_estudiante()
            curso = facultad.buscar_curso("Ingrese el código del curso al que desea inscribirlo: ")

            if estudiante in curso.estudiantesInscriptos:
                print(f"¡Ojo! El estudiante {estudiante.nombre} ya se encuentra inscripto en el curso {curso.nomCurso}.")
                continue

            curso.agregarEst(estudiante)
            if estudiante in curso.estudiantesInscriptos:
                estudiante.inscriptosEn.append(curso)
        elif opcion == "4": # Darse de baja de un curso
            if not facultad.estudiantes or not facultad.cursos:
                print("No se pueden realizar bajas porque faltan registrar estudiantes o cursos.")
                continue
                
            estudiante = facultad.buscar_estudiante()
            curso = facultad.buscar_curso("Ingrese el código del curso del que desea darse de baja: ")

            if estudiante in curso.estudiantesInscriptos:
                curso.eliminarEst(estudiante)
                estudiante.darseBaja(curso) 
                print("Se efectuó la baja con éxito de la lista del estudiante.")
            else:
                print("El estudiante no pertenece a este curso.")

        elif opcion == "5": # Consultar estado de estudiante
            facultad.estado_estudiante()

        elif opcion == "6": # Consultar estado de curso
            facultad.estado_curso()

        elif opcion == "0":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
