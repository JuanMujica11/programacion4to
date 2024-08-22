class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")

    def aplicar_descuento(self):
        if self.precio > 100000:
            self.precio *= 0.9  # Descuento del 10%
            print(f"Precio después del descuento: {self.precio}")
        else:
            print("No aplica descuento.")

class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)

class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)

# Ejemplo de uso
moto1 = Moto("Rojo", 120000)
carro1 = Carro("Azul", 95000)

print("Información de la moto:")
moto1.mostrar_informacion()
moto1.aplicar_descuento()

print("\nInformación del carro:")
carro1.mostrar_informacion()
carro1.aplicar_descuento()