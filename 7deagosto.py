class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 5:
            print("El alumno ha aprobado.")
        else:
            print("El alumno ha reprobado.")

# Ejemplo de uso
alumno1 = Alumno("Juan", 7)
alumno1.imprimir_informacion()
alumno1.resultado()