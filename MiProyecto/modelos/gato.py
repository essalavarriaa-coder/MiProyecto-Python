from modelos.animal import Animal

# Clase derivada Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color, energia=100):
        """
        Inicializa un gato con un nombre, color y nivel de energía.
        :param nombre: Nombre del gato.
        :param color: Color del gato.
        :param energia: Nivel de energía inicial del gato (por defecto 100).
        """
        super().__init__(nombre, "Miau", energia)
        self.color = color

    # Sobreescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        """
        Imprime el maullido del gato, incluyendo su color.
        Reduce la energía del gato al maullar.
        """
        if self._energia > 0:
            print(f"El gato {self._nombre} de color {self.color} maulla: {self.sonido}")
            self._energia -= 8
        else:
            print(f"{self._nombre} está demasiado cansado para maullar.")

    def __str__(self):
        """
        Representación en cadena del objeto Gato.
        :return: Una cadena que describe el gato, incluyendo su color.
        """
        return f"Gato: {self._nombre}, Color: {self.color}, Sonido: {self.sonido}, Energía: {self._energia}"