class Estudiantes():
    def __init__(self, nombre, apellido, nroMat, carrera): 
        self.nombre = nombre.strip().title()
        self.apellido = apellido.strip().title()
        self.nroMat = nroMat.strip()
        self.carrera = carrera.strip().title()
        self.inscriptosEn = []

    def darseBaja(self, curso):
        if curso in self.inscriptosEn:
            self.inscriptosEn.remove(curso)
