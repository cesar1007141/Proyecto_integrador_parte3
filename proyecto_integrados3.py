import os

def clear_screen():
    """
    Función para borrar la pantalla de la terminal según el sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    number = 0

    while number <= 50:
        clear_screen()  # Borra la pantalla antes de imprimir
        print(f"Número actual: {number}")
        try:
            input("Presiona la tecla 'n' para continuar...")
        except KeyboardInterrupt:
            break  # Sale del bucle si se presiona Ctrl+C
        number += 1

if __name__ == "__main__":
    main()
