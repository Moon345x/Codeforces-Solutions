import random

# Lista de números de pines válidos (según el enunciado)
VALID_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              21, 22, 23, 25, 26, 27, 32, 33]

def generate_large_test(M=1_000_000, input_file="input.txt", output_file="output.txt"):
    """
    Genera un caso de prueba con M instrucciones (por defecto 1 millón).
    Escribe la entrada en input_file y la salida esperada en output_file.
    """
    with open(input_file, 'w') as fin, open(output_file, 'w') as fout:
        # Escribir la primera línea con M
        fin.write(f"{M}\n")

        # Diccionario para llevar el estado actual de los pines mencionados
        state = {}

        for _ in range(M):
            # Elegir un pin aleatorio de la lista válida
            pin = random.choice(VALID_PINS)
            # Estado aleatorio 0 o 1 (más rápido con getrandbits)
            e = random.getrandbits(1)

            # Escribir la instrucción en el archivo de entrada
            fin.write(f"GPIO_{pin} {e}\n")

            # Procesar la instrucción para determinar si hay ERROR
            if pin not in state:
                # Primera vez que aparece: estado implícito 0
                if e == 0:
                    fout.write("ERROR\n")
                    state[pin] = 0
                else:
                    state[pin] = 1
            else:
                if state[pin] == e:
                    fout.write("ERROR\n")
                else:
                    state[pin] = e

        # Al final, escribir los pines mencionados ordenados por número
        for pin in sorted(state.keys()):
            fout.write(f"GPIO_{pin} {state[pin]}\n")

    print(f"✅ Caso generado con {M} instrucciones.")
    print(f"   Entrada: {input_file}")
    print(f"   Salida esperada: {output_file}")

if __name__ == "__main__":
    # Fijar semilla para reproducibilidad (opcional)
    random.seed(42)
    generate_large_test()