"""Suite de pruebas para ListaEnlazada y TablaHash."""
import random
from estructuras import ListaEnlazada, TablaHash


def probar_busqueda_basica() -> None:
    """Verifica busquedas exitosas e infructuosas."""
    lista = ListaEnlazada()
    tabla = TablaHash(11)

    lista.insertar(1000000010, "en bodega")
    tabla.insertar(1000000010, "en bodega")

    assert lista.buscar(1000000010) == "en bodega"
    assert tabla.buscar(1000000010) == "en bodega"

    assert lista.buscar(9999999999) is None
    assert tabla.buscar(9999999999) is None


def probar_colision_forzada() -> None:
    """Verifica colision forzada en casilla 3 con m = 7."""
    tabla = TablaHash(7)
    guias_colision = (10, 24, 17)
    for g in guias_colision:
        assert tabla.hash(g) == 3
        tabla.insertar(g, "en bodega")

    for g in guias_colision:
        assert tabla.buscar(g) == "en bodega"

    assert tabla.casillas[3].tamano == 3
    assert tabla.buscar(99) is None
    assert abs(tabla.factor_carga() - (3 / 7)) < 1e-9


def probar_colecciones_aleatorias() -> None:
    """Verifica equivalencia entre lista y tabla en 20 colecciones."""
    azar = random.Random(42)
    estados = ["en bodega", "en reparto", "entregado", "devuelto"]

    for _ in range(20):
        n = azar.randint(10, 50)
        m = 13
        lista = ListaEnlazada()
        tabla = TablaHash(m)

        guias_insertadas: list[int] = []
        for _ in range(n):
            guia = azar.randint(10**9, 10**10 - 1)
            estado = azar.choice(estados)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
            guias_insertadas.append(guia)

        # Verificar guias existentes
        for guia in guias_insertadas[:5]:
            assert lista.buscar(guia) == tabla.buscar(guia)

        # Verificar guias inexistentes
        for _ in range(5):
            guia_falsa = azar.randint(10**9, 10**10 - 1)
            if guia_falsa not in guias_insertadas:
                assert lista.buscar(guia_falsa) is None
                assert tabla.buscar(guia_falsa) is None


if __name__ == "__main__":
    probar_busqueda_basica()
    probar_colision_forzada()
    probar_colecciones_aleatorias()
    print("¡Todas las pruebas pasaron exitosamente!")
