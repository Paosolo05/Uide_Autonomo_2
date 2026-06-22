
"""
Juego: La computadora adivina tu número
----------------------------------------
Tú piensas un número dentro de un rango y la computadora
intenta adivinarlo usando búsqueda binaria (siempre elige
el número del medio entre el mínimo y el máximo posible).

Tú le respondes con:
  - "mayor"    -> si tu número es mayor que el intento
  - "menor"    -> si tu número es menor que el intento
  - "correcto" -> si adivinó tu número
"""


def adivinar_numero():
    print("=" * 50)
    print("JUEGO: LA COMPUTADORA ADIVINA TU NÚMERO")
    print("=" * 50)
    print("Piensa un número entre 1 y 100 (no me lo digas).")
    input("Presiona ENTER cuando estés listo... ")

    minimo = 1
    maximo = 100
    intentos = 0

    while minimo <= maximo:
        intento = (minimo + maximo) // 2
        intentos += 1

        print(f"\nIntento #{intentos}: ¿Tu número es {intento}?")
        respuesta = input(
            "Responde 'mayor', 'menor' o 'correcto': "
        ).strip().lower()

        if respuesta == "correcto":
            print(f"\n¡Excelente! Adiviné tu número ({intento}) "
                  f"en {intentos} intento(s).")
            return
        elif respuesta == "mayor":
            minimo = intento + 1
        elif respuesta == "menor":
            maximo = intento - 1
        else:
            print("Respuesta no válida. Usa 'mayor', 'menor' o 'correcto'.")
            intentos -= 1  # no contar el intento si la respuesta fue inválida

    print("\nHubo una contradicción en tus respuestas, "
          "así que no pude encontrar el número.")


def main():
    while True:
        adivinar_numero()
        otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra_vez != "s":
            print("¡Gracias por jugar!")
            break


if __name__ == "__main__":
    main()
    