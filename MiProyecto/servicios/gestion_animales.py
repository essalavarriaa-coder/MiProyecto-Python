from modelos.animal import Animal
from modelos.perro import Perro
from modelos.gato import Gato

def gestionar_animales():
    """
    Crea y gestiona una lista de animales, demostrando encapsulación.
    """
    animales = []

    # Crear animales
    animal1 = Animal("Generic Animal", "Generic Sound", 80)
    perro1 = Perro("Buddy", "Golden Retriever", 90)
    gato1 = Gato("Whiskers", "Gray", 70)

    # Añadir animales a la lista
    animales.append(animal1)
    animales.append(perro1)
    animales.append(gato1)

    # Imprimir información de los animales
    for animal in animales:
        print(animal)

    # Cambiar el nombre de un animal usando el setter (Encapsulación)
    animal1.set_nombre("New Animal Name")
    print(animal1)