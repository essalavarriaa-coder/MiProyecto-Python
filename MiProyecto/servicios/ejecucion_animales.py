from modelos.animal import Animal
from modelos.perro import Perro
from modelos.gato import Gato

def ejecutar_animales():
    """
    Crea instancias de diferentes animales y demuestra polimorfismo.
    """
    # Crear instancias de las clases
    animal = Animal("Generic Animal", "Generic Sound", 80)
    perro = Perro("Buddy", "Golden Retriever", 90)
    gato = Gato("Whiskers", "Gray", 70)

    # Demostrar polimorfismo: cada animal hace su sonido de forma diferente
    animal.hacer_sonido()
    perro.hacer_sonido()
    gato.hacer_sonido()

    print(animal)
    print(perro)
    print(gato)

    # Demostrar la función de comer
    animal.comer("hierba")
    perro.comer("croquetas")
    gato.comer("pescado")

    print(animal)
    print(perro)
    print(gato)