from servicios.ejecucion_animales import ejecutar_animales
from servicios.gestion_animales import gestionar_animales

def main():
    """
    Función principal que ejecuta las funciones de demostración.
    """
    ejecutar_animales()
    gestionar_animales()

if __name__ == "__main__":
    main()