"""Script de pruebas para las soluciones de subarreglo maximo."""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def probar():
    # Caso de la guia: Serie de 8 dias (suma 17)
    serie_guia = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie_guia)[2] == 17
    assert subarreglo_maximo(serie_guia, 0, len(serie_guia) - 1)[2] == 17

    # Caso: Un solo elemento
    serie_un_elemento = [5.5]
    assert subarreglo_fuerza_bruta(serie_un_elemento)[2] == 5.5
    assert subarreglo_maximo(serie_un_elemento, 0, 0)[2] == 5.5

    # Caso: Todos los valores negativos
    serie_negativos = [-10, -5, -2, -8]
    # El mayor es el elemento menos negativo, o sea -2
    assert subarreglo_fuerza_bruta(serie_negativos)[2] == -2
    assert subarreglo_maximo(serie_negativos, 0, len(serie_negativos) - 1)[2] == -2

    # Caso: Todos los valores positivos
    serie_positivos = [2, 4, 6, 8]
    # La suma de todos es 20
    assert subarreglo_fuerza_bruta(serie_positivos)[2] == 20
    assert subarreglo_maximo(serie_positivos, 0, len(serie_positivos) - 1)[2] == 20

    # Caso: Mejor tramo cruza el punto medio
    serie_cruzada = [-2, -5, 6, -2, -3, 1, 5, -6]
    # El punto medio es indice 3. La mejor racha es [6, -2, -3, 1, 5] que suma 7 y cruza.
    assert subarreglo_fuerza_bruta(serie_cruzada)[2] == 7
    assert subarreglo_maximo(serie_cruzada, 0, len(serie_cruzada) - 1)[2] == 7

    # Caso: Al menos veinte listas aleatorias donde ambas funciones deben dar la misma suma
    random.seed(42) # Semilla fija para reproducibilidad
    for _ in range(20):
        longitud = random.randint(5, 50)
        lista_aleatoria = [random.randint(-100, 100) for _ in range(longitud)]
        
        suma_fuerza = subarreglo_fuerza_bruta(lista_aleatoria)[2]
        suma_divide = subarreglo_maximo(lista_aleatoria, 0, len(lista_aleatoria) - 1)[2]
        
        assert suma_fuerza == suma_divide

    print("¡Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    probar()