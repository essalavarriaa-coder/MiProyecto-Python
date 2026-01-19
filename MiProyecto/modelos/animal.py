# Clase base Animal
class Animal:
    def __init__(self, nombre, sonido, energia=100):
        """
        Inicializa un animal con un nombre, sonido y nivel de energía.
        :param nombre: Nombre del animal.
        :param sonido: Sonido que hace el animal.
        :param energia: Nivel de energía inicial del animal (por defecto 100).
        """
        self._nombre = nombre  # Atributo protegido: convención para indicar que no se debe acceder directamente
        self.sonido = sonido
        self._energia = energia  # Atributo protegido para la encapsulación

    # Getter para el nombre (encapsulación)
    def get_nombre(self):
        """
        Obtiene el nombre del animal.
        :return: El nombre del animal.
        """
        return self._nombre

    # Setter para el nombre (encapsulación)
    def set_nombre(self, nuevo_nombre):
        """
        Establece un nuevo nombre para el animal.
        :param nuevo_nombre: El nuevo nombre del animal.
        """
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena no vacía.")

    def hacer_sonido(self):
        """
        Imprime el sonido que hace el animal.
        Reduce la energía del animal al hacer el sonido.
        """
        if self._energia > 0:
            print(f"El {self._nombre} hace {self.sonido}")
            self._energia -= 10
        else:
            print(f"{self._nombre} está demasiado cansado para hacer un sonido.")

    def comer(self, comida):
        """
        Aumenta la energía del animal al comer.
        :param comida: El tipo de comida que come el animal.
        """
        print(f"{self._nombre} está comiendo {comida}")
        self._energia += 20

    def __str__(self):
        """
        Representación en cadena del objeto Animal.
        :return: Una cadena que describe el animal.
        """
        return f"Animal: {self._nombre}, Sonido: {self.sonido}, Energía: {self._energia}"