class Curso():
    def __init__(self, nomCurso, codCurso, profEncargado, capacidadMaxima): 
        self.nomCurso = nomCurso.strip().title()
        self.codCurso = codCurso.strip()
        self.profEncargado = profEncargado.strip().title()
        self.capacidadMaxima = int(capacidadMaxima)
        self.estudiantesInscriptos = []

    def agregarEst(self, estudiante):
        if self.hayCupos():
            self.estudiantesInscriptos.append(estudiante)
            print(f"Estudiante {estudiante.nombre} agregado al curso con éxito.")
        else:
            print("No se pudo agregar al estudiante porque el curso está lleno.")

    def eliminarEst(self, estudiante):
        if estudiante in self.estudiantesInscriptos:
            self.estudiantesInscriptos.remove(estudiante)
            print(f"Estudiante {estudiante.nombre} dado de baja de {self.nomCurso} con éxito.")
        else:
            print(f"El estudiante {estudiante.nombre} no estaba anotado en este curso.")

    def hayCupos(self):
        return len(self.estudiantesInscriptos) < self.capacidadMaxima
