class Facultad():
    def __init__(self, capacidadMax):
        self.estudiantes = []
        self.cursos = []
        self.capacidadMax = capacidadMax


    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)


    def agregar_curso(self, curso):
        self.cursos.append(curso)


    def buscar_estudiante(self):
        while True:
            mat_buscar = input("Ingrese la matrícula del estudiante: ").strip()
            if mat_buscar == "":
                print("La matrícula no puede estar vacía.")
                continue
            
            for est in self.estudiantes:
                if est.nroMat == mat_buscar:
                    print(f"Estudiante seleccionado: {est.nombre} {est.apellido}")
                    return est
            print("No se encontró ningún estudiante con esa matrícula. Intente de nuevo.")


    def buscar_curso(self, mensaje_pantalla):
        while True:
            cod_buscar = input(mensaje_pantalla).strip()
            if cod_buscar == "":
                print("El código no puede estar vacío.")
                continue

            for cur in self.cursos:
                if cur.codCurso == cod_buscar:
                    print(f"Curso seleccionado: {cur.nomCurso}")
                    return cur
            print("No se encontró ningún curso con ese código. Intente de nuevo.")


    def estado_estudiante(self):
        print("Estado de estudiante: ")
        if not self.estudiantes:
            print("no hay estudiantes inscriptos")
            return

        for estudiante in self.estudiantes:
            nombre_cursos = [curso.nomCurso for curso in estudiante.inscriptosEn]
            curso_string = ", ".join(nombre_cursos) if nombre_cursos else "Ninguno"
            print(f"{estudiante.nombre},{estudiante.apellido},(matricula:{estudiante.nroMat}), - Cursos: [{curso_string}]")


    def estado_curso(self):
        print("Estado de Cursos: ")
        if not self.cursos:
            print("No hay cursos registrados en la facultad.")
            return

        for curso in self.cursos:
            print(f"\nCurso: {curso.nomCurso} (Código: {curso.codCurso})")
            print(f"Profesor encargado: {curso.profEncargado}")
            print("Alumnos pertenecientes a este curso:")
            
            if curso.estudiantesInscriptos:
                for estudiante in curso.estudiantesInscriptos:
                    print(f"  • {estudiante.apellido}, {estudiante.nombre} (Matrícula: {estudiante.nroMat})")
            else:
                print("No hay alumnos anotados en este curso todavía.\n")
