"""
========================================================
PROYECTO_PRIMER_PARCIAL_POO_GRUPO_3
--------------------------------------------------------
Archivo: main.py

Descripción:
Archivo principal del sistema.

Este módulo se encarga de:
- Crear clientes
- Crear servicios
- Probar herencia
- Probar encapsulamiento
- Probar polimorfismo
- Ejecutar reportes
- Validar setters
- Ejecutar el flujo principal del programa

El sistema administra:
- Entradas de cine
- Reservas de eventos
- Gestión de servicios

Autor: Grupo 3
Materia: Programación Orientada a Objetos
========================================================
"""

from ClienteEvento import ClienteEvento
from Entradacine import Entradacine
from ReservaEvento import ReservaEvento
from GestorEventos import GestorEventos


# ====================================================
# FUNCION AUXILIAR
# ====================================================

def separador(titulo=""):

    """
    Imprime separadores visuales en consola.

    Parámetros:
    titulo -> Texto opcional del encabezado.
    """

    linea = "=" * 55

    if titulo:
        print(f"\n{linea}")
        print(f"  {titulo}")
        print(f"{linea}")
    else:
        print(linea)


# ====================================================
# FUNCION PRINCIPAL
# ====================================================

def main():

    """
    Función principal del sistema.

    Ejecuta:
    - Registro de clientes
    - Creación de servicios
    - Polimorfismo
    - Reportes
    - Validaciones
    """

    # ====================================================
    # 1. CREAR CLIENTES
    # ====================================================

    separador("CLIENTES REGISTRADOS")

    cliente1 = ClienteEvento(
        "0912345678",
        "Ana Torres",
        "ana@mail.com",
        "0991234567"
    )

    cliente2 = ClienteEvento(
        "0987654321",
        "Luis Vera",
        "luis@mail.com",
        "0987654321"
    )

    cliente3 = ClienteEvento(
        "",
        "Carlos Rueda",
        "carlos@mail.com",
        "0976543210"
    )

    print(cliente1)
    print(cliente2)
    print(cliente3)

    # ====================================================
    # 2. CREAR OBJETOS DE LAS CLASES HIJAS
    # ====================================================

    separador("SERVICIOS CREADOS")

    entrada1 = Entradacine(
        "EC-001",
        "Avengers: Doomsday",
        "IMAX",
        "noche",
        "general",
        2
    )

    entrada2 = Entradacine(
        "EC-002",
        "Inside Out 3",
        "3D",
        "matinal",
        "estudiante",
        1
    )

    entrada3 = Entradacine(
        "EC-003",
        "Sala invalida",
        "8K",
        "normal",
        "nino",
        3
    )

    reserva1 = ReservaEvento(
        "RE-001",
        "Concierto Rock Nacional",
        4,
        "vip",
        "cena"
    )

    reserva2 = ReservaEvento(
        "RE-002",
        "Festival de Jazz",
        10,
        "preferencial",
        "ninguno"
    )

    reserva3 = ReservaEvento(
        "RE-003",
        "Obra de Teatro",
        5,
        "general",
        "bebidas"
    )

    # ====================================================
    # 3. LISTA POLIMORFICA
    # ====================================================

    """
    Lista que almacena objetos de distintas clases
    hijas usando referencias comunes.
    """

    servicios = [
        entrada1,
        entrada2,
        entrada3,
        reserva1,
        reserva2,
        reserva3
    ]

    # ====================================================
    # 4. IMPRIMIR __str__
    # ====================================================

    separador("REPRESENTACION __str__ DE CADA OBJETO")

    for s in servicios:
        print(s)

    # ====================================================
    # 5. CREAR GESTOR Y AGREGAR SERVICIOS
    # ====================================================

    separador("GESTOR DE EVENTOS")

    gestor = GestorEventos()

    print(gestor)
    print()

    for s in servicios:
        gestor.agregar_servicio(s)

    # ====================================================
    # 6. METODO POLIMORFICO mostrar_info()
    # ====================================================

    gestor.mostrar_reporte()

    # ====================================================
    # 7. METODO POLIMORFICO calcular_total()
    # ====================================================

    separador("TOTAL GLOBAL (calcular_total polimorfico)")

    print(
        f"  Suma de todos los servicios: "
        f"${gestor.calcular_totales():.2f}\n"
    )

    # ====================================================
    # 8. PRUEBAS DE VALIDACION
    # ====================================================

    separador("PRUEBA DE SETTERS CON VALORES INVALIDOS")

    print("Cambiando horario de entrada1 a 'madrugada' (invalido):")

    entrada1.horario = "madrugada"

    print(f"  Horario asignado: {entrada1.horario}")

    print("\nCambiando categoria de entrada2 a '' (vacio):")

    entrada2.categoria = ""

    print(f"  Categoria asignada: {entrada2.categoria}")

    print("\nCambiando num_personas de reserva2 a 0 (invalido):")

    reserva2.num_personas = 0

    print(f"  Personas asignadas: {reserva2.num_personas}")

    print("\nCambiando correo de cliente1 a 'sinArroba' (invalido):")

    cliente1.correo = "sinArroba"

    print(f"  Correo asignado: {cliente1.correo}")

    # ====================================================
    # FIN DEL PROGRAMA
    # ====================================================

    separador("FIN DEL PROGRAMA")


# ====================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ====================================================

if __name__ == "__main__":

    """
    Ejecuta el sistema principal.
    """

    main()