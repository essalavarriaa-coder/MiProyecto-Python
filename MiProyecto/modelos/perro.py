from modelos.animal import Animal

# Clase derivada Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza, energia=100):
        """
        Inicializa un perro con un nombre, raza y nivel de energía.
        :param nombre: Nombre del perro.
        :param raza: Raza del perro.
        :param energia: Nivel de energía inicial del perro (por defecto 100).
        """
        super().__init__(nombre, "Guau", energia)
        self.raza = raza

    # Sobreescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        """
        Imprime el ladrido del perro, incluyendo su raza.
        Reduce la energía del perro al ladrar.
        """
        if self._energia > 0:
            print(f"El perro {self._nombre} de raza {self.raza} ladra: {self.sonido}")
            self._energia -= 15
        else:
            print(f"{self._nombre} está demasiado cansado para ladrar.")

    def __str__(self):
        """
        Representación en cadena del objeto Perro.
        :return: Una cadena que describe el perro, incluyendo su raza.
        """
        return f"Perro: {self._nombre}, Raza: {self.raza}, Sonido: {self.sonido}, Energía: {self._energia}"